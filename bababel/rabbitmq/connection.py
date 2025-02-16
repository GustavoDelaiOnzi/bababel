from bababel.abstracts.connection import Connection
import pika


class RabbitMQConnection(Connection):
    def __init__(self, parameters: pika.ConnectionParameters):
        self.parameters = parameters

    def channel(self):
        return pika.BlockingConnection(parameters=self.parameters)
