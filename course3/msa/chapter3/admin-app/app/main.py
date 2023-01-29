import asyncio
import aio_pika
import aio_pika.abc

import json

from aio_pika import connect
from aio_pika import IncomingMessage

from typing import List

from fastapi import FastAPI, Request, Depends, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from .conn import database
from .schemas import user, order
from .crud import user_crud, order_crud
 
app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.mount("/admin/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/admin")
async def root(request: Request):
    return templates.TemplateResponse("users.html", {"request": request})

@app.get("/admin/view/users", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request})

@app.get("/admin/view/orders", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("orders.html", {"request": request})

@app.get("/admin/users", response_model=List[user.User])
def read_users(db: Session = Depends(get_db)):
    return user_crud.read_all_user(db)

@app.get("/admin/orders", response_model=List[object])
def read_orders(db: Session = Depends(get_db)):
    return order_crud.read_orders(db)



@app.websocket("/admin/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    con = 'amqps://admin:Wmfwmf77azaz!!@b-07655c01-6b7f-4169-ba74-71e0117c313e.mq.ap-northeast-2.amazonaws.com:5671'
    
    connection = await connect(con)
    channel = await connection.channel()

    await channel.set_qos(prefetch_count=1)

    queue = await channel.declare_queue('orders')

    async def on_message(message: IncomingMessage):
        async with message.process():
            await websocket.send_text(f"{message.body}")

    await queue.consume(on_message)

    while True:
        await queue.consume(on_message)
        await asyncio.sleep(1)

