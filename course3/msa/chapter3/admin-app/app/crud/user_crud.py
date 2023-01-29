from sqlalchemy.orm import Session
from app.models.tb_user import TbUser

def read_all_user(db: Session):
    return db.query(TbUser).all()
