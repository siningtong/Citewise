from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # SecretStr hides the value when printed or logged.
    openai_api_key: SecretStr
    openai_model: str = "gpt-5-nano"


settings = Settings()
