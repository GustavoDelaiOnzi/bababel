from unittest.mock import MagicMock

import pytest

from bababel.bababel_app import BababelApp
from bababel.task.task import Task


@pytest.fixture(autouse=True)
def mock_conn(mocker):
    yield mocker.patch('bababel.rabbitmq.rabbitmq_connection.BlockingConnection', MagicMock())


class SampleTask(Task):
    def run(self, message: str, code: int):
        return f'{message}-{code}'


class TestIntegrationSend:
    def test_should_basic_publish(self, mock_conn):
        app = BababelApp(host='localhost',
                         port=5672,
                         username='guest',
                         password='guest')

        task = SampleTask(app=app)
        task.send(message='xpto', code=123)

        mock_conn.return_value.channel.return_value.basic_publish.assert_called_once_with(
            exchange=app.identifier,
            routing_key='sample_task',
            body=b'{"message": "xpto", "code": 123}',
            properties=None
        )
