import pika
import json

from app.schemas.order import Order, OrderCreate
from fastapi.encoders import jsonable_encoder

rabbitmq_user = '<username>'
rabbitmq_password = '<password>'
rabbitmq_broker_id = '<broker-id>'
region = 'ap-northeast-2'
MQ_URL = f"amqps://{rabbitmq_user}:{rabbitmq_password}@{rabbitmq_broker_id}.mq.{region}.amazonaws.com:5671"

params = pika.URLParameters(MQ_URL)

class PikaClient:
    def __init__(self):
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()


    def is_open(self):
        return self.channel.is_open

    def pub_order(self, orderCreare):
        queue = 'orders'

        self.channel.queue_declare(queue)

        messgage = json.dumps(jsonable_encoder(orderCreare))

        self.channel.basic_publish(
            exchange='',
            routing_key=queue,
            body=messgage
        )

        return messgage