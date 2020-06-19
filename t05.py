class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


# Pen (ручка), Pencil (карандаш), Handle (маркер)

class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка Ручкой(Pen) {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка карандашом(Pencil) {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка маркером(Handle) {self.title}")


a = Stationery("generic")
a.draw()
b = Pen("mypen")
b.draw()
c = Pencil("mypencil")
c.draw()
d = Handle("myhandle")
d.draw()
