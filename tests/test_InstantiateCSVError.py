import pytest

from src.item import InstantiateCSVError


@pytest.fixture
def properties_instantiatecsverror():
    return InstantiateCSVError()


def test_init():
    error = InstantiateCSVError()
    assert error.message == 'Файл item.csv поврежден'
