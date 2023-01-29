from typing import List
import uuid
from datetime import datetime

from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from .conn import database
from .conn.pika_client import PikaClient
from .schemas import product, order
from .crud import product_crud, order_crud
 
app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

mq_client = PikaClient()

@app.get("/", response_class=HTMLResponse)
async def read_products(request: Request):
    return templates.TemplateResponse("order.html", {"request": request})

@app.get("/products", response_model=List[product.Product])
def read_products(db: Session = Depends(get_db)):
    return product_crud.read_products(db)

# @app.post("/order", response_model=order.Order)
@app.post("/order")
def create_order(order: order.OrderCreate, db: Session = Depends(get_db)):
    order_crud.create_order(order, db)

    order.order_id = str(uuid.uuid1())
    order.created = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    new_order = order_crud.get_order(order, db)
    return mq_client.pub_order(new_order)

@app.get("/is_open_channel")
def is_open_channel():
    return mq_client.is_open()