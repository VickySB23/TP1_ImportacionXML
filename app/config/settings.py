class DatabaseSettings:
    @property
    def url(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
    
    user = "sysacad"
    password = "sysacad2025"
    host = "localhost"
    port = "5432"
    name = "DEV_SYSACAD"

db_settings = DatabaseSettings()