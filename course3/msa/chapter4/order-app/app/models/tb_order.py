from sqlalchemy import Column, TEXT, INT, DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TbOrder(Base):
    __tablename__ = "tb_order"

    order_id = Column(TEXT, nullable=False, primary_key=True)
    product_id = Column(INT, nullable=False)
    user_id = Column(INT, nullable=False)
    created = Column(DATETIME, nullable=True)