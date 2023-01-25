import uuid
from datetime import datetime

from typing import Optional
from pydantic import BaseModel

class Order(BaseModel):
    order_id : Optional[str] = str(uuid.uuid1())
    product_id : int
    user_id : int
    created : Optional[str] = datetime.now().strftime("%Y-%m-%d %H:%M:%s")

    class Config:
        orm_mode = True

class OrderCreate(Order):
    pass