from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_URL: str
    EMAIL: str
    PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()