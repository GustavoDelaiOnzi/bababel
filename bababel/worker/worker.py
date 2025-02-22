from typing import List, Optional

from bababel.abstracts.client import IClient
from bababel.abstracts.connection import IConnection
from bababel.dataclasses.queue_callback_bind import QueueCallbackBind
from bababel.rabbitmq.rabbitmq_client import RabbitMQClient


class Worker:
    """
    Worker class responsible for consuming messages from RabbitMQ queues.

    This class establishes a connection to RabbitMQ using the RabbitMQClient,
    binds queues to their respective callback functions, and starts consuming messages.

    Attributes:
        client (IClient): The RabbitMQ client used to establish a connection.
        connection (IConnection): The established connection to RabbitMQ.
        queue_callback_binds (List[QueueCallbackBind]): A list of queue-to-callback bindings.
    """

    def __init__(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        queue_callback_binds: Optional[List[QueueCallbackBind]] = None,
    ):
        """
        Initializes the Worker instance and establishes a RabbitMQ connection.

        Args:
            host (str): The RabbitMQ server hostname or IP address.
            port (int): The port number for the RabbitMQ service.
            username (str): The username for authentication.
            password (str): The password for authentication.
            queue_callback_binds (Optional[List[QueueCallbackBind]]):
                A list of QueueCallbackBind objects containing queue names and their callbacks.
        """
        self.client: IClient = RabbitMQClient()
        self.connection: IConnection = self.client.connect(host=host, port=port, username=username, password=password)
        self.queue_callback_binds = queue_callback_binds or []

    def declare_bind(self, queue_callback_bind: QueueCallbackBind) -> None:
        """
        Declares a queue using a specified callback function.

        Args:
            queue_callback_bind (QueueCallbackBind):
                An object containing the queue name and the callback function to handle messages.
        """
        self.connection.queue_declare(queue=queue_callback_bind.queue, durable=True)
        self.connection.basic_consume(
            queue=queue_callback_bind.queue, on_message_callback=queue_callback_bind.callback
        )

    def start(self):
        self.connection.process_events()
