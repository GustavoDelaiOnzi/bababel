from unittest.mock import MagicMock

import pytest

from bababel.publisher.publisher import Publisher


@pytest.fixture(autouse=True)
def mock_connect(mocker):
    yield mocker.patch('bababel.publisher.publisher.RabbitMQClient', MagicMock())


class TestPublisher:
    @pytest.fixture
    def sut(self):
        return Publisher(app=MagicMock())

    def test_should_publish(self, sut, mock_connect):
        sut.publish(task_name='xpto', body={'xpto': 'xpto'})
        sut.connection.publish.assert_called_once_with(exchange=sut.app.identifier,
                                                       routing_key='xpto',
                                                       body=b'{"xpto": "xpto"}')
