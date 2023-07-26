import csv


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = 'Файл item.csv поврежден'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        Item.all.append(self)
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @staticmethod
    def string_to_number(string_num):
        if '.' in string_num:
            return int(float(string_num))
        return int(string_num)

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open('../src/items.csv', 'r', newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                cls.all.clear()
                for row in reader:
                    if len(row) != 3:
                        raise InstantiateCSVError
                    else:
                        cls(**row)
        except FileNotFoundError:
            print('Отсутствует файл item.csv')


def calculate_total_price(self) -> float:
    """
    Рассчитывает общую стоимость конкретного товара в магазине.
    :return: Общая стоимость товара.
    """
    return float(self.price * self.quantity)


def apply_discount(self) -> None:
    """
    Применяет установленную скидку для конкретного товара.
    """
    self.price *= self.pay_rate
