from dataclasses import dataclass


@dataclass(init=False)
class DbSettings:
    port: int
    host: str
    database: str


class DevSettings:
    def __init__(self):
        self.db = DbSettings()
        self.db.host = "localhost"
        self.db.port = 27017


class Settings(DevSettings):
    pass


setting = Settings()

