from .base import Crud
from ..models.order import OrderCreate, OrderOut, OrderInDb, ItemOrder
import uuid
from ..enumerator import StateEnum
import datetime


class OrderCrud(Crud):
    def get_ids_of_items(self, items):
        return [x.item_id for x in items]

    async def create(self, db, documento: OrderCreate, id=None, user=None) -> OrderOut:
        items = []
        async for item in db.items.find(
            {"ID": {"$in": self.get_ids_of_items(documento.items)}}
        ):
            for order_item in documento.items:
                if item["ID"] == order_item.item_id:
                    item["amount"] = order_item.amount
                    items.append(ItemOrder(**item))

        if id:
            id = uuid.UUID(id)
        else:
            id = uuid.uuid4()
        order_dict = {
            "items": items,
            "ID": id,
            "state": StateEnum.WAIT_PAYMENT.value,
            "create_at": datetime.datetime.now(),
            "user_id": id,
        }
        order = OrderInDb(**order_dict)
        result = await db.orders.insert_one(order.dict())
        return OrderOut(**order.dict())