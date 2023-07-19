import pytest

from src.phone import Phone


@pytest.fixture
def properties_phone():
    return Phone('Lenovo', 20000, 3, 3)


def test_init_(properties_phone):
    assert properties_phone.name == 'Lenovo'
    assert properties_phone.price == 20000
    assert properties_phone.quantity == 3
    assert properties_phone.sim_count == 3


def test_repr_(properties_phone):
    assert repr(properties_phone) == "Phone('Lenovo', 20000, 3, 3)"


def test_number_of_sim_setter(properties_phone):
    properties_phone.number_of_sim = 4
    assert properties_phone.number_of_sim == 4
    with pytest.raises(ValueError):
        properties_phone.number_of_sim = 0



