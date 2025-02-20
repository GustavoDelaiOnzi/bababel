import pytest

from bababel.dataclasses.queue_callback_bind import QueueCallbackBind


@pytest.fixture
def binds():
    def func_1():
        return 'xpto1'

    def func_2():
        return 'xptp2'

    def func_3():
        return 'xpto3'

    return [
        QueueCallbackBind(queue='queue1', callback=func_1),
        QueueCallbackBind(queue='queue2', callback=func_2),
        QueueCallbackBind(queue='queue3', callback=func_3)
    ]