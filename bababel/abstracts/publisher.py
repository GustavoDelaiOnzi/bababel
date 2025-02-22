from abc import ABC, abstractmethod


class IPublisher(ABC):
    @abstractmethod
    def publish(self, *args, **kwargs):
        ...