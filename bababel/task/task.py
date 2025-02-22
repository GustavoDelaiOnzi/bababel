import re

from abc import ABC, abstractmethod

from bababel.bababel_app import BababelApp


class Task(ABC):
    """
    Abstract base class for defining asynchronous tasks.

    This class enforces the structure for task execution by requiring subclasses
    to implement the `run` method and define a `app` attribute.

    Example:
        Creating and executing a task:

        class HelloWorld(Task)
            def run(*args, **kwargs):
                print('Hello World')

        task = HelloWorld(app="example")
        task.run(*args, **kwargs)

        Alternatively, you can call the task instance directly:

        task(*args, **kwargs)

    Attributes:
        name (str): The class name, set dynamically. It is also the identifier of the task and must be unique.
    """

    def __new__(cls, *args, **kwargs):
        """
        Creates a new instance of a Task subclass.
        """
        instance = super().__new__(cls)
        cls.name = re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()  # Converts to snake case
        # TODO: make a utils function

        return instance

    def __init__(self, app: BababelApp):
        """
        Args:
            app (BababelApp): The app to be assigned to the instance.
        """
        self.app = app

    def __call__(self, *args, **kwargs):
        """Allows the instance to be called like a function."""
        self.run(*args, **kwargs)

    @abstractmethod
    def run(self, *args, **kwargs):
        """The main process of the task."""
        raise NotImplementedError()
