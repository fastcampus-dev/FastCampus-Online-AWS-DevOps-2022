from sqlalchemy.orm import Session
from app.models.tb_product import TbProduct

def read_products(db: Session):
    return db.query(TbProduct).all()
