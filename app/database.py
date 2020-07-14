import motor.motor_asyncio
from app.settings import setting

client = motor.motor_asyncio.AsyncIOMotorClient(setting.db.uri)
db = client[setting.db.database]


def get_db():
    return db
