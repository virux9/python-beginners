from operator import add


class Matrix:
    def __init__(self, in_list):
        self.m_list = in_list
        pass

    def __str__(self):
        out_str = ""
        for i in self.m_list:
            for j in i:
                out_str += str(j) + "\t"
            out_str += "\n"
        return out_str

    def __add__(self, other):
        out_list = []
        for i in range(0, len(self.m_list)):
            out_list.append(list(map(add, self.m_list[i], other.m_list[i])))
        return Matrix(out_list)


a = Matrix([[12, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[12, 42, 13], [14, 5, 16], [27, 38, 9]])

print("a =")
print(a)
print("b =")
print(a)
print("a + b =")
print(a + b)
