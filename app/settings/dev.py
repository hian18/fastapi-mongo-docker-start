from dataclasses import dataclass


@dataclass(init=False)
class DbSettings:
    port: int
    host: str
    database: str
    uri: str


class DevSettings:
    SECRET_KEY: str = "secret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    def __init__(self):
        self.db = DbSettings()
        self.db.host = "localhost"
        # self.db.host = "mongo"
        self.db.port = 27017
        self.db.database = "python"
        self.db.uri = f'mongodb://{"root"}:{"example"}@{self.db.host}:{self.db.port}/?authSource=admin'
