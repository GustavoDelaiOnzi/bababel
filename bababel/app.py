import nanoid

from bababel.rabbitmq.client import RabbitMQClient
from bababel.routers.message_router import MessageRouter


class BababelApp:
    """
    BababelApp is the main object of this lib. An instance of this object should be provided to the Tasks for
    publishing. Receives the connection parameters to establish a connection and have a unique identifier
    randomly generated.
    """

    def __init__(self, host: str, port: int, username: str, password: str):
        """
        Creates a instance of the BababelApp object.

        :param host: The hostname or IP address of the broker server.
        :param port: The port number on which the broker is running.
        :param username: The username for authentication.
        :param password: The password for authentication.
        """
        self.identifier = nanoid.generate()
        self.client = RabbitMQClient()
        self.connection = self.client.connect(host=host,
                                              port=port,
                                              username=username,
                                              password=password)  # TODO make a connector class
        self.router = MessageRouter(connection=self.connection, identifier=self.identifier)
