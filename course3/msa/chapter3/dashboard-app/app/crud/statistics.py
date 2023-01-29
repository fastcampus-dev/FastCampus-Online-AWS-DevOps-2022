from sqlalchemy.orm import Session
from sqlalchemy.sql import func


from app.models.tb_order import TbOrder

def read_statistics(db: Session):
    orders = db.query(func.substr(TbOrder.created, 1, 10).label('created'), func.count(TbOrder.order_id).label('count'))\
        .group_by(func.substr(TbOrder.created, 1, 10)).order_by(func.substr(TbOrder.created, 1, 10).asc()).all()

    return orders
