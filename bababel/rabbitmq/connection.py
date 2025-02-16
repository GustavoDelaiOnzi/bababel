from pika.adapters.blocking_connection import BlockingConnection
from pika.connection import ConnectionParameters

from bababel.abstracts.connection import Connection


class RabbitMQConnection(Connection):
    def __init__(self, parameters: ConnectionParameters):
        self.parameters = parameters

    def establish(self):
        return BlockingConnection(parameters=self.parameters)
