from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # SecretStr hides the value when printed or logged.
    openai_api_key: SecretStr
    openai_model: str = "gpt-5-nano"
    # How much the model "thinks" before answering. Lower is faster and cheaper,
    # but may lower answer quality. Not every model supports every value.
    openai_reasoning_effort: Literal[
        "none", "minimal", "low", "medium", "high", "xhigh", "max"
    ] = "low"


settings = Settings()
