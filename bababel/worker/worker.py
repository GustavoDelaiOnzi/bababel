from typing import List

from bababel.abstracts.client import IClient
from bababel.abstracts.connection import Connection
from bababel.dataclasses.queue_callback_bind import QueueCallbackBind
from bababel.rabbitmq.rabbitmq_client import RabbitMQClient


class Worker:
    def __init__(
        self, host: str, port: int, username: str, password: str, queue_callback_binds: List[QueueCallbackBind] = None
    ):
        self._client: IClient = RabbitMQClient()
        self._connection: Connection = self._client.connect(host=host, port=port, username=username, password=password)
        self._queue_callback_binds = queue_callback_binds

    def consume_bind(self, queue_callback_bind: QueueCallbackBind) -> None:
        self._connection.queue_declare(queue=queue_callback_bind.queue, durable=True)
        self._connection.basic_consume(
            queue=queue_callback_bind.queue, on_message_callback=queue_callback_bind.callback
        )
        self._connection.start_consuming()
