from bababel.abstracts.publisher import IPublisher
from bababel.enums import BrokerTypeEnum
from bababel.rabbitmq.connection import RabbitMQConnection
from bababel.rabbitmq.publisher import RabbitMQPublisher
from bababel.routers.exceptions import MessageRouterException
from bababel.tasks.task import Task


class MessageRouter:
    def __init__(self, connection, identifier: str):
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
        return self._publisher.publish(task=task, event=event)
