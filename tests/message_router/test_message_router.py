from unittest.mock import MagicMock

import pytest

from bababel.exceptions.exceptions import MessageRouterException
from bababel.message_router import MessageRouter
from bababel.rabbitmq.rabbitmq_connection import RabbitMQConnection


class TestMessageRouter:
    @pytest.fixture
    def sut(self, mocker):
        mocker.patch('bababel.message_router.message_router.RabbitMQPublisher')
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
