class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, weight=25, thickness=1):
        return f'{(self._length * self._width * weight * thickness) / 1000}'


road1 = Road(5000, 20)
print(road1.calc_mass())
# print(vars(road1))
# print(road1._length)
