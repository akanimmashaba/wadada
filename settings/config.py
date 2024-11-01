from pydantic_settings import BaseSettings
from pydantic import PostgresDsn
from supabase import create_client, Client

class Settings(BaseSettings):
    DATABASE_URL: str
    SUPABASE_URL: str
    SUPABASE_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)