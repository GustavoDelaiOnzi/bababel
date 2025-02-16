from abc import ABC, abstractmethod


class Connection(ABC):
    @abstractmethod
    def channel(self):  # TODO add Channel interface
        raise NotImplementedError()
