from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel):
    product_id : int
    product_img : str
    product_name : str
    product_desc : Optional[str] = None
    price : int
    delivery_fee : int
    uploaded : datetime
    seller : int

    class Config:
        orm_mode = True