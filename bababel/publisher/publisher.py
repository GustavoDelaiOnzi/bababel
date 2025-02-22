from bababel.abstracts.client import IClient
from bababel.abstracts.publisher import IPublisher
from bababel.bababel_app import BababelApp
from bababel.rabbitmq.rabbitmq_client import RabbitMQClient


class Publisher(IPublisher):
    def __init__(self, app: BababelApp):
        self.client: IClient = RabbitMQClient()
        self.connection = self.client.connect(host=app.host,
                                              port=app.port,
                                              username=app.username,
                                              password=app.password)

    def publish(self):
        raise NotImplementedError()
