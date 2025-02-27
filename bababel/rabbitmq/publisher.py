from bababel.abstracts.publisher import IPublisher
from bababel.rabbitmq.connection import RabbitMQConnection
from bababel.tasks.task import Task
from bababel.utils import dict_to_bytes


class RabbitMQPublisher(IPublisher):
    def __init__(self, connection: RabbitMQConnection, exchange: str):
        self.connection = connection
        self.exchange = exchange
        self.__declare_rabbitmq_exchange()

    def publish(self, task: Task, event: dict):
        self.connection.publish(exchange=self.exchange,
                                routing_key=task.name,
                                body=dict_to_bytes(event))

    def __declare_rabbitmq_exchange(self):
        self.connection.declare_exchange(exchange=self.exchange)
