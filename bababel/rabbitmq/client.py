from pika.adapters.blocking_connection import BlockingConnection
from pika.connection import ConnectionParameters
from pika.credentials import PlainCredentials

from bababel.abstracts.client import IClient


class RabbitMQClient(IClient):
    def connect(self, host: str, port: int, username: str, password: str) -> BlockingConnection:
        credentials = PlainCredentials(username=username, password=password)

        params = ConnectionParameters(host=host, port=port, credentials=credentials)

        return BlockingConnection(parameters=params)
