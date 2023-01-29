import asyncio
import aio_pika

from aio_pika import ExchangeType, connect
from aio_pika.abc import AbstractIncomingMessage

rabbitmq_user = '<user>'
rabbitmq_password = '<password>'
rabbitmq_broker_id = '<broker-id>'
region = 'ap-northeast-2'
MQ_URL = f"amqps://{rabbitmq_user}:{rabbitmq_password}@{rabbitmq_broker_id}.mq.{region}.amazonaws.com:5671"







    