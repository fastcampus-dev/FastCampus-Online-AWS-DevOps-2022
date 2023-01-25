from typing import Optional
from pydantic import BaseModel

class Order(BaseModel):
    order_id : Optional[str] = ''
    product_id : int
    user_id : int
    created : Optional[str] = ''

    class Config:
        orm_mode = True

class OrderCreate(Order):
    pass