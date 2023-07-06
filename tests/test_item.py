"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def properties_item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(properties_item):
    assert properties_item.calculate_total_price() == 200000


def test_apply_discount(properties_item):
    properties_item.pay_rate = 0.8
    properties_item.apply_discount()
    assert properties_item.price == 8000.0
