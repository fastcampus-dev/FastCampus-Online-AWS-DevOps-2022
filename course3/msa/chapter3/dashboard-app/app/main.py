from json import loads
from kafka import KafkaConsumer
import json

# from aiokafka import AIOKafkaConsumer
# from confluent_kafka import Consumer
from kafka import KafkaConsumer, KafkaProducer
from fastapi import FastAPI, Request, Depends, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from .conn import database
from .crud import statistics

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.mount("/dashboard/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/dashboard/statistics")
async def dashboard(db: Session = Depends(get_db)):
    return statistics.read_statistics(db)


@app.websocket("/dashboard/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    consumer = KafkaConsumer('orders',
                         group_id='my-group',
                         bootstrap_servers=['b-1.mskcluster2.kk9qho.c2.kafka.ap-northeast-2.amazonaws.com:9092'])
    
    for message in consumer:
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value))
        websocket.send_text(f"{message.value}")