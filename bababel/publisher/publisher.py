from bababel.rabbitmq.rabbitmq_client import RabbitMQClient


class Publisher:
    def __init__(self, host: str, port: int, username: str, password: str):
        self.client = RabbitMQClient()
        self.connection = self.client.connect(host=host, port=port, username=username, password=password)

    def publish(self):
        raise NotImplementedError()
