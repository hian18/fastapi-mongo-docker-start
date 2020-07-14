import motor.motor_asyncio
from .settings import setting

client = motor.motor_asyncio.AsyncIOMotorClient(setting.db.host, setting.db.port)
db = client[setting.db.database]

