from bababel.rabbitmq.rabbitmq_client import RabbitMQClient


class Publisher:
    def __init__(self, app):
        self.client = RabbitMQClient()
        self.connection = self.client.connect(host=app.host,
                                              port=app.port,
                                              username=app.username,
                                              password=app.password)
        self.app = app

    def publish(self, task_name: str, body: str | bytes):
        self.connection.publish(exchange=self.app.identifier,
                                routing_key=task_name,
                                body=body)
