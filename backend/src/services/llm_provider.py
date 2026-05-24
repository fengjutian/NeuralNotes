"""LLM Provider abstraction for multiple AI backends.

Supports OpenAI, Zhipuai (Qwen/DeepSeek), and other providers.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional

from openai import RateLimitError, APIError

from src.config import settings
from src.utils.logging import get_logger
from src.utils.exceptions import AIProviderException, AIRateLimitException

logger = get_logger(__name__)


@dataclass
class LLMResponse:
    """Response from LLM API."""

    content: Optional[str]
    model: str
    usage: dict[str, int]


class BaseLLMProvider(ABC):
    """Abstract base class for LLM providers."""

    @abstractmethod
    def chat_completion(
        self,
        messages: list[dict[str, str]],
        **kwargs: Any,
    ) -> LLMResponse:
        """Generate chat completion."""
        pass

    @abstractmethod
    def supports_streaming(self) -> bool:
        """Check if provider supports streaming."""
        pass


class OpenAIProvider(BaseLLMProvider):
    """OpenAI API provider."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gpt-4",
        base_url: Optional[str] = None,
        max_retries: int = 3,
    ) -> None:
        self.api_key = api_key or settings.openai_api_key
        self.model = model
        self.base_url = base_url or settings.openai_base_url
        self.max_retries = max_retries
        self.logger = get_logger(self.__class__.__name__)

    def chat_completion(
        self,
        messages: list[dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs: Any,
    ) -> LLMResponse:
        from openai import OpenAI

        client = OpenAI(api_key=self.api_key, base_url=self.base_url)

        try:
            response = client.chat.completions.create(
                model=model or self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs,
            )

            content = response.choices[0].message.content or ""
            usage = {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens,
            }

            return LLMResponse(
                content=content,
                model=response.model,
                usage=usage,
            )

        except RateLimitError as e:
            self.logger.error("Rate limit exceeded")
            raise AIRateLimitException() from e

        except APIError as e:
            self.logger.error("OpenAI API error: %s", str(e))
            raise AIProviderException(provider="OpenAI", message=str(e)) from e

    def supports_streaming(self) -> bool:
        return True


class ZhipuaiProvider(BaseLLMProvider):
    """Zhipuai API provider."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "glm-4",
        max_retries: int = 3,
    ) -> None:
        self.api_key = api_key or settings.zhipuai_api_key
        self.model = model
        self.max_retries = max_retries
        self.logger = get_logger(self.__class__.__name__)

        try:
            import zhipuai
            self.zhipuai = zhipuai
        except ImportError:
            self.logger.warning("zhipuai package not installed")
            self.zhipuai = None

    def chat_completion(
        self,
        messages: list[dict[str, str]],
        **kwargs: Any,
    ) -> LLMResponse:
        if not self.zhipuai:
            raise AIProviderException(provider="Zhipuai", message="zhipuai package not installed")

        try:
            response = self.zhipuai.model_api.invoke(model=self.model, prompt=messages)
            content = response.get("data", {}).get("choices", [{}])[0].get("content", "")
            return LLMResponse(content=content, model=self.model, usage={})
        except Exception as e:
            self.logger.error("Zhipuai API error: %s", str(e))
            raise AIProviderException(provider="Zhipuai", message=str(e)) from e

    def supports_streaming(self) -> bool:
        return True


class LLMProvider:
    """Unified LLM provider."""

    PROVIDER_MAP = {
        "openai": OpenAIProvider,
        "zhipuai": ZhipuaiProvider,
    }

    def __init__(
        self,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        self.provider_name = provider or settings.ai_provider
        self.model = model or settings.openai_model
        self.logger = get_logger(self.__class__.__name__)

        provider_class = self.PROVIDER_MAP.get(self.provider_name)
        if not provider_class:
            raise ValueError(f"Unknown provider: {self.provider_name}")

        self._provider = provider_class(**kwargs)
        self.logger.info("Initialized LLM provider: %s (model: %s)", self.provider_name, self.model)

    @property
    def provider(self) -> str:
        return self.provider_name

    def chat_completion(self, messages: list[dict[str, str]], **kwargs: Any) -> LLMResponse:
        return self._provider.chat_completion(messages, **kwargs)

    def supports_streaming(self) -> bool:
        return self._provider.supports_streaming()