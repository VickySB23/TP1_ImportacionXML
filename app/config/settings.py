import os

class DatabaseSettings:
    @property
    def url(self) -> str:
        user = os.getenv("DB_USER", "sysacad")
        password = os.getenv("DB_PASSWORD", "sysacad2025")
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", "5432")
        name = os.getenv("DB_NAME", "DEV_SYSACAD")
        return f"postgresql://{user}:{password}@{host}:{port}/{name}"

db_settings = DatabaseSettings()