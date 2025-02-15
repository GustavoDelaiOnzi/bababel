from bababel.rabbitmq.client import RabbitMQClient


class Worker:
    def __init__(self):
        self.connection = None
        self.client = RabbitMQClient()

    def connect(self, host: str, port: int, username: str, password: str):
        self.connection = self.client.connect(host=host, port=port, username=username, password=password)
