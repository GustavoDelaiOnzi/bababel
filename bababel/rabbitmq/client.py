from pika.connection import ConnectionParameters
from pika.credentials import PlainCredentials

from bababel.abstracts.client import IClient
from bababel.abstracts.connection import Connection
from bababel.rabbitmq.connection import RabbitMQConnection


class RabbitMQClient(IClient):
    def connect(self, host: str, port: int, username: str, password: str) -> Connection:
        credentials = PlainCredentials(username=username, password=password)

        params = ConnectionParameters(host=host, port=port, credentials=credentials)

        return RabbitMQConnection(parameters=params)
