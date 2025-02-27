from unittest.mock import MagicMock

import pytest

from bababel.rabbitmq.connection import RabbitMQConnection
from bababel.routers.exceptions import MessageRouterException
from bababel.routers.message_router import MessageRouter


class TestMessageRouter:
    @pytest.fixture
    def sut(self, mocker):
        mocker.patch('bababel.routers.message_router.RabbitMQPublisher')
        yield MessageRouter(connection=MagicMock(spec=RabbitMQConnection), identifier='xpto')

    def test_should_publish(self, sut):
        task = MagicMock()

        response = sut.publish(task=task, event={})

        assert response == sut._publisher.publish.return_value
        sut._publisher.publish.assert_called_once_with(task=task, event={})

    def test_should_raise_broker_type(self):
        conn = MagicMock()

        with pytest.raises(MessageRouterException) as exc:
            MessageRouter(connection=conn, identifier='xpto')

        assert exc.value.message == f"Couldn't find a broker for the given connection: {conn.__str__}"
