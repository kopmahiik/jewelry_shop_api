from pydantic import model_validator
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    DB_HOST: str
    DB_NAME: str
    DB_PASS: str
    DB_PORT: int
    DB_USER: str
    DEBUG_MODE: bool
    MEDIA_URL: str = ""

    DATABASE_URL: str = ""

    @model_validator(mode="after")
    def set_database_url(self):
        self.DATABASE_URL = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return self

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = AppSettings()
