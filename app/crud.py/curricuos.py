from ..database import db


class CurriculoCrud:
    async def create(self, documento):
        result = await db.curriculos.insert_one(documento)
        documento.id = result.inserted_id

