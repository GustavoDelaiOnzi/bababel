import nanoid

from bababel.rabbitmq.client import RabbitMQClient
from bababel.routers.message_router import MessageRouter


class BababelApp:
    def __init__(self, host: str, port: int, username: str, password: str):
        self.identifier = nanoid.generate()
        self.client = RabbitMQClient()
        self.connection = self.client.connect(host=host,
                                              port=port,
                                              username=username,
                                              password=password)  # TODO make a connector class
        self.router = MessageRouter(connection=self.connection, identifier=self.identifier)
