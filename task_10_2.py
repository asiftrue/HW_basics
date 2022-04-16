from abc import ABC, abstractmethod


class Clothes(ABC):
    fab = 0

    @abstractmethod
    def calc_fab(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = float(size)
        Coat.fab += self.calc_fab

    def __str__(self):
        return f'Расход ткани на пальто {self.calc_fab}, общий расход ткани на пальто {Coat.fab:02f}'

    @property
    def calc_fab(self):
        fabric = self.size / 6.5 + 0.5
        return float(f'{fabric:02f}')


class Suit(Clothes):
    def __init__(self, height):
        self.height = float(height)
        Suit.fab += self.calc_fab

    def __str__(self):
        return f'Расход ткани на костюм {self.calc_fab:02f}, общий расход ткани на костюмы {Suit.fab:02f}'

    @property
    def calc_fab(self):
        fabric = self.height * 2 + 0.3
        return float(fabric)


coat1 = Coat(60)
print(coat1)
coat2 = Coat(56)
print(coat2)
suit1 = Suit(1.80)
print(suit1)
suit2 = Suit(1.72)
print(suit2)

