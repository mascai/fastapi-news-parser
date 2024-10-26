import os
from pydantic_settings import BaseSettings, SettingsConfigDict


DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str
    DB_PASSWORD: str
    DB_USER: str

    model_config = SettingsConfigDict(env_file=DOTENV)


settings = Settings()