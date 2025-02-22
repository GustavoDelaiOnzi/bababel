from abc import ABC, abstractmethod


class IConnection(ABC):
    """
    Abstract base class defining the interface for a connection.
    """

    @abstractmethod
    def queue_declare(self, *args, **kwargs) -> None:
        """
        Declare a queue with the given parameters.
        """
        raise NotImplementedError()

    @abstractmethod
    def basic_consume(self, *args, **kwargs) -> None:
        """
        Consume messages from a queue.
        """
        raise NotImplementedError()

    @abstractmethod
    def start_consuming(self, *args, **kwargs) -> None:
        """
        Start consuming messages from the queue.
        """
        raise NotImplementedError()

    @abstractmethod
    def process_events(self, *args, **kwargs):
        raise NotImplementedError()
