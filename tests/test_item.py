"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture


def properties_Item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(properties_Item):
    assert properties_Item.calculate_total_price() == 200000


def test_apply_discount(properties_Item):
    Item.pay_rate = 0.8
    properties_Item.apply_discount()
    assert properties_Item.price == 8000.0
