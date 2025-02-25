import pytest

from bababel.utils.singleton import SingletonMeta


class TestSingletonMeta:
    @pytest.fixture
    def sut(self):
        class XptoSingleton(metaclass=SingletonMeta):
            pass

        return XptoSingleton()

    def test_should_init(self, sut):
        pass
