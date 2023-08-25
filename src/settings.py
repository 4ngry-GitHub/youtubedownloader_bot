from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_token: str
    log_level: str

    class Config:
        env_file = ".env"


settings = Settings()
