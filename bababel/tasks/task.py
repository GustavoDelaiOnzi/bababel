import inspect
from abc import ABC, abstractmethod

from bababel.tasks.exceptions import TaskError
from bababel.utils import camel_to_snake


class Task(ABC):
    """
    Abstract base class for creating Bababel Tasks.
    Subclasses must implement the `run` method, which will serve as a template for the `send` method, responsible
    for sending the task for a worker to process.
    """
    def __new__(cls, *args, **kwargs):
        """
        Creates a new instance of the `Task` object and declares `name` class attribute.

        :param args:
        :param kwargs:
        :returns: A instance of the `Task` object.
        """
        instance = super().__new__(cls)
        cls.name = camel_to_snake(cls.__name__)
        return instance

    def __init__(self, app):
        """
        :param app:
        :type app: bababel.app.BababelApp
        """
        self.app = app

    @abstractmethod
    def run(self, *args, **kwargs):
        """
        This is the method that will executed by the worker.
        """
        raise NotImplementedError()

    def send(self, *args, **kwargs):
        """
        Sends the task for a worker to execute later.

        :param args:
        :param kwargs:
        :return:
        :raises TaskError: If the arguments provided diverge from the `run` method arguments.
        """
        self._inspect_arguments(*args, **kwargs)
        self.app.router.publish(task=self, event=self._get_body(*args, **kwargs))

    def _inspect_arguments(self, *args, **kwargs):
        sig = inspect.signature(self.run)
        try:
            sig.bind(*args, **kwargs)
        except TypeError as e:
            expected_params = ', '.join(
                f"{name}: {param.annotation.__name__}"
                for name, param in sig.parameters.items()
            )
            received_args = ', '.join(
                f"{name}: {value}"
                for name, value in zip(sig.parameters, args)
            )
            received_kwargs = ', '.join(
                f"{key}: {value}"
                for key, value in kwargs.items()
            )
            raise TaskError(
                "Invalid arguments: "
                f"Expected (parameters: {expected_params}), "
                f"got (args: {received_args}, kwargs: {received_kwargs})"
            ) from e

    def _get_body(self, *args, **kwargs):
        param_names = list(inspect.signature(self.__class__.run).parameters.keys())[1:]
        args_dict = {name: value for name, value in zip(param_names, args)}
        args_dict.update(kwargs)
        return args_dict
