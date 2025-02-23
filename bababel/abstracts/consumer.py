from abc import ABC, abstractmethod

from bababel.dataclasses.queue_callback_bind import QueueCallbackBind


class IConsumer(ABC):
    @abstractmethod
    def declare_bind(self, queue_callback_bind: QueueCallbackBind):
        raise NotImplementedError()

    @abstractmethod
    def start(self):
        raise NotImplementedError()
