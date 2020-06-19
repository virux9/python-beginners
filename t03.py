class Worker:
    def __init__(self, name_in, surname_in, position_in, wage, bonus):
        self.name = name_in
        self.surname = surname_in
        self.position = position_in
        self._income = {"wage": wage, "bonus": bonus}

    def calc_mass(self, area):
        return self._length * self._width * self._mass * area


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position("Ivan", "Petrov", "Analyst", 10000, 5000)
print(p.get_full_name())
print(p.get_total_income())
