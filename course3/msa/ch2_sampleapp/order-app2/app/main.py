from typing import List

from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from . import database
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

@app.get("/", response_class=HTMLResponse)
async def read_products(request: Request):
    return templates.TemplateResponse("order.html", {"request": request})

@app.get("/products", response_model=List[product.Product])
def read_products(db: Session = Depends(get_db)):
    return product_crud.read_products(db)

@app.post("/order", response_model=order.Order)
def create_order(order: order.OrderCreate, db: Session = Depends(get_db)):
    return order_crud.create_order(order, db)

