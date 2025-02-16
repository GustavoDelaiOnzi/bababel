from abc import ABC, abstractmethod


class Connection(ABC):
    @abstractmethod
    def queue_declare(self, *args, **kwargs): ...

    @abstractmethod
    def basic_consume(self, *args, **kwargs): ...

    @abstractmethod
    def start_consuming(self, *args, **kwargs): ...
