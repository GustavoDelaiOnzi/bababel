from typing import List

from bababel.abstracts.client import IClient
from bababel.abstracts.connection import Connection
from bababel.abstracts.queue_callback_bind import QueueCallbackBind
from bababel.rabbitmq.client import RabbitMQClient


class Worker:
    def __init__(self,
                 host: str,
                 port: int,
                 username: str,
                 password: str,
                 queue_callback_binds: List[QueueCallbackBind] = None):
        self._client: IClient = RabbitMQClient()
        self._connection: Connection = self._connect(host=host, port=port, username=username, password=password)
        self._channel = None
        self._queue_callback_binds = queue_callback_binds

    def _connect(self, host: str, port: int, username: str, password: str) -> Connection:
        return self._client.connect(host=host, port=port, username=username, password=password)

    def consume(self, queue_callback_bind: QueueCallbackBind) -> None:
        self._ensure_channel()
        self._channel.queue_declare(queue=queue_callback_bind.queue,
                                    durable=True)
        self._channel.basic_consume(queue=queue_callback_bind.queue,
                                    on_message_callback=queue_callback_bind.callback,
                                    auto_ack=False)
        self._channel.start_consuming()

    def _ensure_channel(self) -> None:
        if not self._channel:
            self._channel = self._connection.channel()
