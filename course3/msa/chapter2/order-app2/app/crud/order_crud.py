import uuid
from datetime import datetime

from sqlalchemy.orm import Session
from app.models.tb_order import TbOrder
from app.schemas.order import OrderCreate

def create_order(order: OrderCreate, db):
    order.order_id = str(uuid.uuid1())
    
    created = datetime.now()
    order.created = created.strftime("%Y-%m-%d %H:%M:%s")

    db_order = TbOrder(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order
