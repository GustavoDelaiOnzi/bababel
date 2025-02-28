from bababel.abstract.publisher import IPublisher
from bababel.rabbitmq.rabbitmq_connection import RabbitMQConnection
from bababel.task.task import Task
from bababel.utils.utils import dict_to_bytes


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
