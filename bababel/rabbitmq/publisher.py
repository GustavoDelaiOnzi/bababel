from bababel.abstracts.publisher import IPublisher
from bababel.rabbitmq.connection import RabbitMQConnection
from bababel.tasks.task import Task
from bababel.utils import dict_to_bytes


class RabbitMQPublisher(IPublisher):
    """
    Handles message publishing to a RabbitMQ broker.
    """

    def __init__(self, connection: RabbitMQConnection, exchange: str):
        """
        Creates a instance of the RabbitMQPublisher object.

        :param connection: A `bababel.rabbitmq.connection.RabbitMQConnection` instance.
        :param exchange: The RabbitMQ broker exchange name to publish messages to.
        """
        self.connection = connection
        self.exchange = exchange

    def publish(self, task: Task, event: dict):
        """
        Publishes a message to the object exchange.
        Declares the exchange in RabbitMQ broker if it is not yet declared.

        :param task: A `bababel.tasks.task.Task` instance.
        :param event: The event payload data to publish.
        :return:
        """
        self._declare_rabbitmq_exchange()
        self.connection.publish(exchange=self.exchange,
                                routing_key=task.name,
                                body=dict_to_bytes(event))

    def _declare_rabbitmq_exchange(self):
        self.connection.declare_exchange(exchange=self.exchange)
