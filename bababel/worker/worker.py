from typing import List

from bababel.abstracts.client import IClient
from bababel.abstracts.queue_callback_bind import QueueCallbackBind
from bababel.rabbitmq.client import RabbitMQClient


class Worker:
    def __init__(self,
                 host: str,
                 port: int,
                 username: str,
                 password: str):
        self._client: IClient = self._set_client(RabbitMQClient())
        self._connection = self._connect(host=host, port=port, username=username, password=password)
        self._channel = None
        self._queues: List[str] = []

    def _connect(self, host: str, port: int, username: str, password: str):
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

    def _set_client(self, client: IClient) -> IClient:
        return client
