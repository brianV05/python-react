from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 43200
    JWT_ISSUER: str = "api.cafeorders.com"  # Default value if not set in the environment

    class Config:
        env_file = ".env"


settings = Settings()