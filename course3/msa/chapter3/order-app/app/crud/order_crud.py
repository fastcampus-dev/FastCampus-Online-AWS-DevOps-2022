import uuid
from datetime import datetime

from sqlalchemy.orm import Session
from app.models.tb_order import TbOrder
from app.models.tb_product import TbProduct
from app.models.tb_user import TbUser
from app.schemas.order import OrderCreate

def create_order(order: OrderCreate, db):
    order.order_id = str(uuid.uuid1())
    
    created = datetime.now()
    order.created = created.strftime("%Y-%m-%dT%H:%M:%S")

    db_order = TbOrder(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order

def get_order(order: OrderCreate, db):
    product_name = db.query(TbProduct.product_name).filter(TbProduct.product_id == order.product_id).first()
    user_name = db.query(TbUser.user_name).filter(TbUser.user_id == order.user_id).first()
    
    new_order = {}
    new_order['order_id'] = order.order_id
    new_order['product_name'] = product_name[0]
    new_order['user_name'] = user_name[0]
    new_order['created'] = order.created

    return new_order

    
