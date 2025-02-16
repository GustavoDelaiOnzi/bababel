from dataclasses import dataclass
from typing import Callable


@dataclass
class QueueCallbackBind:
    queue: str
    callback: Callable
