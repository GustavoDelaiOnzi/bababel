import nanoid

from bababel.message_router.message_router import MessageRouter
from bababel.rabbitmq.rabbitmq_client import RabbitMQClient


class BababelApp:
    def __init__(self, host: str, port: int, username: str, password: str):
        self.identifier = nanoid.generate()
        self.client = RabbitMQClient()
        self.connection = self.client.connect(host=host,
                                              port=port,
                                              username=username,
                                              password=password)  # TODO make a connector class
        self.router = MessageRouter(connection=self.connection, identifier=self.identifier)
