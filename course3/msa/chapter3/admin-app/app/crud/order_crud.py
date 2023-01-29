import datetime
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.models.tb_order import TbOrder
from app.models.tb_user import TbUser
from app.models.tb_product import TbProduct

def read_orders(db: Session):
    orders = (db.query(TbOrder.order_id, TbProduct.product_name, TbUser.user_name, TbOrder.created)\
        .join(TbUser, TbOrder.user_id == TbUser.user_id)\
        .join(TbProduct, TbOrder.product_id == TbProduct.product_id).order_by(desc(TbOrder.created)))[:100]

    return orders
