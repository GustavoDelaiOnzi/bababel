import inspect
from abc import ABC, abstractmethod

from bababel.tasks.exceptions import TaskError
from bababel.utils import camel_to_snake


class Task(ABC):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.name = camel_to_snake(cls.__name__)
        return instance

    def __init__(self, app):
        self.app = app

    @abstractmethod
    def run(self, *args, **kwargs):
        raise NotImplementedError()

    def send(self, *args, **kwargs):
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
