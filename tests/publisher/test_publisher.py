from unittest.mock import MagicMock

import pytest

from bababel.publisher import RabbitMQPublisher


class TestPublisher:
    @pytest.fixture
    def sut(self):
        return RabbitMQPublisher(connection=MagicMock(), exchange='xpto_exchange')

    def test_should_publish(self, sut):
        task = MagicMock()

        sut.publish(task=task, event={'xpto': 'xpto'})

        sut.connection.publish.assert_called_once_with(exchange=sut.exchange,
                                                       routing_key=task.name,
                                                       body=b'{"xpto": "xpto"}')
