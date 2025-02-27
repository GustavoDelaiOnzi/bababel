from abc import ABC, abstractmethod

from bababel.task.task import Task


class IPublisher(ABC):
    @abstractmethod
    def publish(self, task: Task, event: dict):
        raise NotImplementedError()
