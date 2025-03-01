from pika.connection import ConnectionParameters
from pika.credentials import PlainCredentials

from bababel.abstracts.client import IClient
from bababel.rabbitmq.connection import RabbitMQConnection


class RabbitMQClient(IClient):
    """
    The RabbitMQClient handles connection operations with a RabbitMQ broker.
    """
    def connect(self, host: str, port: int, username: str, password: str) -> RabbitMQConnection:
        """
        Creates a connection instance of a RabbitMQ broker.

        :param host: The hostname or IP address of the RabbitMQ server.
        :param port: The port number on which RabbitMQ is running.
        :param username: The username for authentication.
        :param password: The password for authentication.
        :return: A `bababel.rabbitmq.connection.RabbitMQConnection` instance.
        """
        credentials = PlainCredentials(username=username, password=password)

        params = ConnectionParameters(host=host, port=port, credentials=credentials)

        return RabbitMQConnection(parameters=params)
