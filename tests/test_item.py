"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

import pytest

from src.item import Item


@pytest.fixture
def properties_item():
    return Item('Смартфон_Lenovo_Laptop', 10000, 20)


def test_init_properties_item(properties_item):
    item = Item('Смартфон_Lenovo_Laptop', 10000, 20)
    assert item.name == 'Смартфон_Lenovo_Laptop'
    assert item.price == 10000
    assert item.quantity == 20


def test_calculate_total_price(properties_item):
    assert properties_item.calculate_total_price() == 200000


def test_apply_discount(properties_item):
    properties_item.pay_rate = 0.8
    properties_item.apply_discount()
    assert properties_item.price == 8000.0


def test_name_setter(properties_item):
    item1 = Item('Смартфон_Lenovo_Laptop', 10000, 20)
    item2 = Item('Смартфон', 10000, 20)
    if len(item1.name) >= 10:
        assert item1.name[0:10] == 'Смартфон_L'
    elif len(item2.name) < 10:
        assert item2.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    with open('../tests/test.csv', 'w', newline='') as csvfile:
        _writer = csv.writer(csvfile)
        _writer.writerow(['name', 'price', 'quantity'])
        _writer.writerow(['Lenovo', '2000', '1'])
        _writer.writerow(['sony', '1000', '5'])
        _writer.writerow(['MacBook', '5000', '2'])
    Item.all = []
    with open('../tests/test.csv', 'r', newline='') as csvfil:
        reader = csv.DictReader(csvfil)
        for row in reader:
            Item(**row)

    assert len(Item.all) == 3
    assert Item.all[1].price == '1000'
    assert Item.all[2].name == 'MacBook'
    assert Item.all[0].quantity == '1'
