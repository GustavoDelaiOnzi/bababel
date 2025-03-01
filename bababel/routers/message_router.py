from bababel.abstracts.publisher import IPublisher
from bababel.enums import BrokerTypeEnum
from bababel.rabbitmq.connection import RabbitMQConnection
from bababel.rabbitmq.publisher import RabbitMQPublisher
from bababel.routers.exceptions import MessageRouterException
from bababel.tasks.task import Task


class MessageRouter:
    """
    MessageRouter publishes a message to the correct broker based on the connection it receives.
    For example, if it receives a RabbitMQ connection it publishes the message using the correct Bababel Publisher,
    in this case `bababel.rabbitmq.publisher.RabbitMQPublisher`
    """
    def __init__(self, connection, identifier: str):
        """
        Creates a instance of MessageRouter object.

        :param connection: A Bababel connection instance.
        :param identifier: Should be a `bababel.app.BababelApp` instance identifier.
        """
        self.connection = connection
        self.identifier = identifier
        self._publisher: IPublisher = self.__set_publisher()

    def __set_publisher(self) -> IPublisher:
        broker_type = self.__set_broker_type()

        publisher = {
            BrokerTypeEnum.RABBITMQ.value: RabbitMQPublisher(connection=self.connection, exchange=self.identifier)
        }.get(broker_type)
        if not publisher:
            raise ValueError("Couldn't find publisher for given 'broker_type'")  # pragma: no cover
        return publisher

    def __set_broker_type(self) -> BrokerTypeEnum:
        if isinstance(self.connection, RabbitMQConnection):
            return BrokerTypeEnum.RABBITMQ.value
        raise MessageRouterException(f"Couldn't find a broker for the given connection: {self.connection.__str__}")

    def publish(self, task: Task, event: dict):
        """
        Publish the message to the correct broker based on the received connection.

        :param task:  A `bababel.tasks.task.Task` instance.
        :param event: The event payload data to publish.
        :return:
        """
        return self._publisher.publish(task=task, event=event)
