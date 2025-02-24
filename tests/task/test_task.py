from unittest.mock import MagicMock

import pytest

from bababel.exceptions.base_bababel_error import TaskError
from bababel.task.task import Task


class TestTask:
    @pytest.fixture
    def sut(self):
        class XptoTask(Task):
            def run(self, message: str, message2: str):
                return message + message2

        return XptoTask(app=MagicMock())

    def test_should_run(self, sut):
        response = sut.run('xpto', message2='xpto2')

        assert response == 'xptoxpto2'

    def test_should_send(self, sut):
        body = {
            'message': 'xpto',
            'message2': 'xpto2'
        }

        sut.send('xpto', message2='xpto2')

        sut.app.publisher.publish.assert_called_once_with(task_name=sut.name, body=body)

    def test_should_raise_send(self, sut):
        with pytest.raises(TaskError) as exc:
            sut.send('xpto', wrong_arg='xpto2')
        assert (exc.value.message == 'Invalid arguments: Expected (parameters: message: str, '
                                     'message2: str), got (args: message: xpto, kwargs: wrong_arg: xpto2)')
