from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "LocalTrust-NAP"
    supabase_url: str = ""
    supabase_key: str = ""
    google_api_key: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
