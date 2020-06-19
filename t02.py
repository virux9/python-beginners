class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._mass = 25

    def calc_mass(self, area):
        return self._length * self._width * self._mass * area


rd = Road(20, 5000)
print(rd.calc_mass(5))
