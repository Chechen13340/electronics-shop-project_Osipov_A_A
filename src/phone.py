from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim_count: int) -> None:
        super().__init__(name, price, quantity)
        if isinstance(sim_count, int) and sim_count > 0:
            self.__sim_count = sim_count
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__sim_count})"

    @property
    def number_of_sim(self):
        return self.__sim_count

    @number_of_sim.setter
    def number_of_sim(self, count):
        if isinstance(count, int) and count > 0:
            self.__sim_count = count
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
