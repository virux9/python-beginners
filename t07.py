class ComplexNumber:
    def __init__(self, part_a, part_b):
        self.part_a = part_a
        self.part_b = part_b

    def __str__(self):
        if self.part_b >= 0:
            return f"{self.part_a}+{self.part_b}i"
        else:
            return f"{self.part_a}{self.part_b}i"

    def __add__(self, other):
        return ComplexNumber(self.part_a + other.part_a, self.part_b + other.part_b)

    def __mul__(self, other):
        return ComplexNumber((self.part_a * other.part_a) - (self.part_b * other.part_b),
                             (self.part_a * other.part_b) + (other.part_a * self.part_b))


a = ComplexNumber(1, -2)
b = ComplexNumber(3, 4)
print(f"a = {a}")
print(f"b = {b}")
print(f"a * b = {a * b}")
print(f"a + b = {a + b}")
