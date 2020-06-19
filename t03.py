class Cell:
    def __init__(self, number_of_el):
        self.number_of_el = int(number_of_el)

    def __add__(self, other):
        return Cell(self.number_of_el + other.number_of_el)

    def __sub__(self, other):
        res = self.number_of_el - other.number_of_el
        if res > 0:
            return Cell(res)
        else:
            print("subtraction result is negative")
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.number_of_el * other.number_of_el)

    def __truediv__(self, other):
        return Cell(self.number_of_el // other.number_of_el)

    def make_order(self, num_row):
        j = 0
        out_str = ""
        for i in range(0, self.number_of_el):
            out_str += "*"
            j += 1
            if j >= num_row:
                j = 0
                out_str += "\n"
        return out_str


c1 = Cell(20)
c2 = Cell(13)
print(f"c1={c1.number_of_el}")
print(f"c2={c2.number_of_el}")
c3 = c1 + c2
print(f"c1+c2={c3.number_of_el}")
c4 = c1 - c2 - c2
print(f"c1-c2={c4.number_of_el}")
c5 = c1 * c2
print(f"c1*c2={c5.number_of_el}")
c6 = c1 / c2
print(f"c1/c2={c6.number_of_el}")
print(c2.make_order(5))
