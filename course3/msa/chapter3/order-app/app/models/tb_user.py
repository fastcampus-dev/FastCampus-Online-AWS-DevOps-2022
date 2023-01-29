from sqlalchemy import Column, TEXT, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TbUser(Base):
    __tablename__ = "tb_user"

    user_id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    user_name = Column(TEXT, nullable=True)
    user_email = Column(TEXT, nullable=True)
    user_pw = Column(TEXT, nullable=True)
    street_address = Column(TEXT, nullable=True)
    address_line_2 = Column(TEXT, nullable=True)
    phone = Column(INT, nullable=True)