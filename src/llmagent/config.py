from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str | None = None
    azure_vault_url: str | None = None
    model: str = "gpt-3.5-turbo"

settings = Settings()
