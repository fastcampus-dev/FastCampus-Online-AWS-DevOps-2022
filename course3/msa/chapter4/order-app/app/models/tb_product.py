from sqlalchemy import Column, TEXT, INT, DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TbProduct(Base):
    __tablename__ = "tb_product"

    product_id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    product_img = Column(TEXT, nullable=True)
    product_name = Column(TEXT, nullable=True)
    product_desc = Column(TEXT, nullable=True)
    price = Column(INT, nullable=True)
    delivery_fee = Column(INT, nullable=True)
    uploaded = Column(DATETIME, nullable=True)
    seller = Column(INT, nullable=True)