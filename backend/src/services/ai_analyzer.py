"""AI Analyzer service for batch processing highlights."""

import asyncio
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Optional

from src.services.llm_provider import LLMProvider
from src.services.concept_extractor import ConceptExtractor, ExtractedConcepts
from src.utils.logging import get_logger

logger = get_logger(__name__)


class JobStatus(str, Enum):
    """Analysis job status."""

    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class AnalysisJob:
    """Represents an analysis job."""

    job_id: str
    status: JobStatus
    total: int
    completed: int = 0
    errors: int = 0
    results: list[ExtractedConcepts] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    @property
    def progress_percent(self) -> float:
        if self.total == 0:
            return 100.0
        return (self.completed / self.total) * 100

    def to_dict(self) -> dict[str, Any]:
        return {
            "job_id": self.job_id,
            "status": self.status.value,
            "total": self.total,
            "completed": self.completed,
            "errors": self.errors,
            "progress_percent": self.progress_percent,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


class AIAnalyzer:
    """AI analyzer for batch processing highlights."""

    def __init__(
        self,
        llm_provider: Optional[LLMProvider] = None,
        concept_extractor: Optional[ConceptExtractor] = None,
        batch_size: int = 10,
        max_retries: int = 3,
    ) -> None:
        self.llm_provider = llm_provider or LLMProvider()
        self.extractor = concept_extractor or ConceptExtractor(
            llm_provider=self.llm_provider
        )
        self.batch_size = batch_size
        self.max_retries = max_retries
        self.logger = get_logger(self.__class__.__name__)
        self._jobs: dict[str, AnalysisJob] = {}

    def create_job(
        self,
        highlights: list[dict[str, Any]],
        book_id: Optional[str] = None,
    ) -> str:
        """Create a new analysis job."""
        job_id = str(uuid.uuid4())
        job = AnalysisJob(
            job_id=job_id,
            status=JobStatus.PENDING,
            total=len(highlights),
        )
        self._jobs[job_id] = job
        self.logger.info("Created analysis job %s with %d highlights", job_id, len(highlights))
        return job_id

    def get_job_status(self, job_id: str) -> AnalysisJob:
        """Get job status and results."""
        if job_id not in self._jobs:
            raise ValueError(f"Job not found: {job_id}")
        return self._jobs[job_id]

    def cancel_job(self, job_id: str) -> bool:
        """Cancel a running job."""
        job = self.get_job_status(job_id)
        if job.status in (JobStatus.COMPLETED, JobStatus.FAILED):
            return False
        job.status = JobStatus.CANCELLED
        job.updated_at = datetime.now()
        self.logger.info("Cancelled job %s", job_id)
        return True

    def _divide_into_batches(
        self,
        highlights: list[dict[str, Any]],
    ) -> list[list[dict[str, Any]]]:
        """Divide highlights into batches."""
        batches = []
        for i in range(0, len(highlights), self.batch_size):
            batches.append(highlights[i : i + self.batch_size])
        return batches

    def _update_job_progress(
        self,
        job_id: str,
        completed_count: int,
        error_count: int = 0,
    ) -> None:
        """Update job progress."""
        job = self._jobs[job_id]
        job.completed += completed_count
        job.errors += error_count
        job.updated_at = datetime.now()
        if job.completed >= job.total:
            job.status = JobStatus.COMPLETED if job.errors == 0 else JobStatus.FAILED

    async def analyze_highlight(
        self,
        highlight: dict[str, Any],
        retries: int = 0,
    ) -> ExtractedConcepts:
        """Analyze a single highlight."""
        content = highlight.get("content", "")
        if not content:
            return ExtractedConcepts(concepts=[], domain=None, emotion="neutral")

        try:
            result = await asyncio.get_event_loop().run_in_executor(
                None,
                self.extractor.extract,
                content,
            )
            return result
        except Exception as e:
            if retries < self.max_retries:
                self.logger.warning("Analysis failed, retrying (%d/%d): %s", retries + 1, self.max_retries, str(e))
                await asyncio.sleep(2 ** retries)
                return await self.analyze_highlight(highlight, retries + 1)
            self.logger.error("Analysis failed after %d retries: %s", self.max_retries, str(e))
            raise

    async def process_job(
        self,
        job_id: str,
        highlights: list[dict[str, Any]],
    ) -> AnalysisJob:
        """Process all highlights in a job."""
        job = self.get_job_status(job_id)
        job.status = JobStatus.PROCESSING
        job.updated_at = datetime.now()
        self.logger.info("Starting job %s: %d highlights", job_id, len(highlights))

        batches = self._divide_into_batches(highlights)
        total_errors = 0

        for batch_idx, batch in enumerate(batches):
            if job.status == JobStatus.CANCELLED:
                break

            batch_results = []
            batch_errors = 0

            for highlight in batch:
                try:
                    result = await self.analyze_highlight(highlight)
                    batch_results.append(result)
                except Exception:
                    batch_results.append(ExtractedConcepts(concepts=[], domain=None, emotion="neutral"))
                    batch_errors += 1

            job.results.extend(batch_results)
            total_errors += batch_errors
            self._update_job_progress(job_id, completed_count=len(batch_results), error_count=batch_errors)

        job.updated_at = datetime.now()
        if job.completed >= job.total:
            job.status = JobStatus.COMPLETED if total_errors == 0 else JobStatus.FAILED

        return job

    def analyze_highlights(self, highlights: list[dict[str, Any]]) -> list[Optional[ExtractedConcepts]]:
        """Synchronous highlight analysis (blocking)."""
        results = []
        for highlight in highlights:
            try:
                result = self.extractor.extract(highlight.get("content", ""))
                results.append(result)
            except Exception as e:
                self.logger.error("Analysis failed: %s", str(e))
                results.append(None)
        return results

    def get_all_jobs(self) -> list[AnalysisJob]:
        """Get all jobs."""
        return list(self._jobs.values())

    def cleanup_completed_jobs(self, older_than_hours: int = 24) -> int:
        """Clean up old completed jobs."""
        cutoff = datetime.now().timestamp() - (older_than_hours * 3600)
        to_remove = []
        for job_id, job in self._jobs.items():
            if job.status in (JobStatus.COMPLETED, JobStatus.FAILED):
                if job.updated_at.timestamp() < cutoff:
                    to_remove.append(job_id)
        for job_id in to_remove:
            del self._jobs[job_id]
        self.logger.info("Cleaned up %d old jobs", len(to_remove))
        return len(to_remove)


# Singleton instance
ai_analyzer = AIAnalyzer()