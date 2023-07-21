import pytest

from src.keyboard import Keyboard


@pytest.fixture
def properties_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_init_(properties_keyboard):
    assert properties_keyboard.name == 'Dark Project KD87A'
    assert properties_keyboard.price == 9600
    assert properties_keyboard.quantity == 5


def test_str_(properties_keyboard):
    assert str(properties_keyboard) == 'Dark Project KD87A'


def test_language(properties_keyboard):
    assert properties_keyboard.language == 'EN'


def test_change_lang(properties_keyboard):
    properties_keyboard.change_lang()
    assert properties_keyboard.language == 'RU'
    properties_keyboard.change_lang().change_lang()
    assert properties_keyboard.language == 'RU'
    properties_keyboard.change_lang().change_lang().change_lang()
    assert properties_keyboard.language == 'EN'
