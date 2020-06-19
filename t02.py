from abc import ABC, abstractmethod


class AbstractClothing(ABC):
    @abstractmethod
    def __init__(self, name):
        pass


class Clothing(AbstractClothing):
    def __init__(self, name):
        super().__init__(name)
        self.name = name


class Coat(Clothing):
    def __init__(self, name, volume):
        self.volume = volume
        super().__init__(name)

    @property
    def cloth_needed(self):
        return self.volume / 6.5 + 0.5


class Costume(Clothing):
    def __init__(self, name, height):
        self.height = height
        super().__init__(name)

    @property
    def cloth_needed(self):
        return 2 * self.height + 0.3


coat_1 = Coat("coat1", 10)
costume_1 = Costume("costume1", 180)
print(f"Total cloth needed: {costume_1.cloth_needed + coat_1.cloth_needed}")
