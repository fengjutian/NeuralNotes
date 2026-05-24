"""Embedding service for text vectorization.

Handles text embedding using sentence transformers.
"""

from typing import Optional

from sentence_transformers import SentenceTransformer

from src.utils.logging import get_logger

logger = get_logger(__name__)


class EmbeddingService:
    """Service for generating text embeddings.

    Uses sentence-transformers for local embedding generation.
    """

    DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    def __init__(
        self,
        model_name: Optional[str] = None,
        device: str = "cpu",
    ) -> None:
        """Initialize embedding service.

        Args:
            model_name: Sentence transformer model name.
            device: Device to use (cpu/cuda).
        """
        self.model_name = model_name or self.DEFAULT_MODEL
        self.device = device
        self._model: Optional[SentenceTransformer] = None
        self.logger = get_logger(self.__class__.__name__)

    @property
    def model(self) -> SentenceTransformer:
        """Lazy load the model."""
        if self._model is None:
            self.logger.info("Loading embedding model: %s", self.model_name)
            self._model = SentenceTransformer(self.model_name, device=self.device)
            self.logger.info("Embedding model loaded")
        return self._model

    @property
    def embedding_dim(self) -> int:
        """Get embedding dimension."""
        return self.model.get_sentence_embedding_dimension()

    def embed_single(self, text: str) -> list[float]:
        """Generate embedding for a single text.

        Args:
            text: Text to embed.

        Returns:
            Embedding vector as list of floats.
        """
        embedding = self.model.encode(text, convert_to_numpy=True)
        return embedding.tolist()

    def embed_batch(
        self,
        texts: list[str],
        batch_size: int = 32,
        show_progress: bool = False,
    ) -> list[list[float]]:
        """Generate embeddings for multiple texts.

        Args:
            texts: List of texts to embed.
            batch_size: Batch size for processing.
            show_progress: Show progress bar.

        Returns:
            List of embedding vectors.
        """
        if not texts:
            return []

        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=show_progress,
            convert_to_numpy=True,
        )

        return [emb.tolist() for emb in embeddings]

    def similarity(
        self,
        text1: str,
        text2: str,
    ) -> float:
        """Calculate cosine similarity between two texts.

        Args:
            text1: First text.
            text2: Second text.

        Returns:
            Similarity score (0-1).
        """
        emb1 = self.embed_single(text1)
        emb2 = self.embed_single(text2)

        # Cosine similarity
        dot = sum(a * b for a, b in zip(emb1, emb2))
        norm1 = sum(a * a for a in emb1) ** 0.5
        norm2 = sum(b * b for b in emb2) ** 0.5

        if norm1 == 0 or norm2 == 0:
            return 0.0

        return dot / (norm1 * norm2)


# Singleton instance
embedding_service = EmbeddingService()
