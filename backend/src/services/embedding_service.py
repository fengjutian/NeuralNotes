"""Embedding service for text vectorization.

Handles text embedding using sentence transformers.
Import is lazy-loaded to avoid startup failures on Windows.
"""

import os
from typing import Optional

from src.utils.logging import get_logger

logger = get_logger(__name__)

# Suppress noisy warnings
os.environ.setdefault("TRANSFORMERS_NO_ADVISORY_WARNINGS", "1")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")


def _import_sentence_transformer():
    """Lazy import sentence_transformers (may fail on Windows)."""
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer


class EmbeddingService:
    """Service for generating text embeddings.

    Uses sentence-transformers for local embedding generation.
    On platforms where it's unavailable, returns zero vectors.
    """

    DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    def __init__(
        self,
        model_name: Optional[str] = None,
        device: str = "cpu",
    ) -> None:
        self.model_name = model_name or self.DEFAULT_MODEL
        self.device = device
        self._model = None
        self._dim: int = 384
        self._available = None  # Lazy check
        self.logger = get_logger(self.__class__.__name__)
        self.logger.info("Embedding service initialized (lazy load enabled)")

    @property
    def is_available(self) -> bool:
        """Check if embedding is available on this platform."""
        if self._available is None:
            try:
                _import_sentence_transformer()
                self._available = True
            except Exception as e:
                self.logger.warning("sentence_transformers not available: %s", e)
                self._available = False
        return self._available

    @property
    def model(self):
        """Lazy load the sentence transformer model."""
        if self._model is None:
            if not self.is_available:
                raise RuntimeError("sentence_transformers is not available")
            SentenceTransformer = _import_sentence_transformer()
            self.logger.info("Loading embedding model: %s", self.model_name)
            self._model = SentenceTransformer(self.model_name, device=self.device)
            self._dim = self._model.get_sentence_embedding_dimension()
            self.logger.info("Embedding model loaded (dim=%d)", self._dim)
        return self._model

    @property
    def embedding_dim(self) -> int:
        return self._dim

    def embed_single(self, text: str) -> list[float]:
        if not self.is_available:
            self.logger.warning("Embedding not available, returning zero vector")
            return [0.0] * self._dim
        embedding = self.model.encode(text, convert_to_numpy=True)
        return embedding.tolist()

    def embed_batch(
        self,
        texts: list[str],
        batch_size: int = 32,
        show_progress: bool = False,
    ) -> list[list[float]]:
        if not texts:
            return []
        if not self.is_available:
            self.logger.warning("Embedding not available, returning zero vectors")
            return [[0.0] * self._dim for _ in texts]
        self.model  # Trigger load
        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=show_progress,
            convert_to_numpy=True,
        )
        return [emb.tolist() for emb in embeddings]

    def similarity(self, text1: str, text2: str) -> float:
        emb1 = self.embed_single(text1)
        emb2 = self.embed_single(text2)
        dot = sum(a * b for a, b in zip(emb1, emb2))
        norm1 = sum(a * a for a in emb1) ** 0.5
        norm2 = sum(b * b for b in emb2) ** 0.5
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot / (norm1 * norm2)


# Singleton instance
embedding_service = EmbeddingService()