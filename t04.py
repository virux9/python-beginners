class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f"Car {self.name} is moving")

    def stop(self):
        print(f"Car {self.name} stopped")

    def turn(self, direction):
        print(f"Car {self.name} is turning to {direction}")

    def show_speed(self):
        print(f"Car {self.name} speed is {self.speed} km/h")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Warning! Car speed is more than 60 km/h !")


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Warning! Car speed is more than 40 km/h !")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


c = TownCar(61, "blue", "ford", True)
c.go()
c.show_speed()
c.stop()

d = WorkCar(50, "red", "kamatsu", False)
d.go()
d.show_speed()
d.stop()

e = SportCar(100, "red", "ferrari", False)
e.go()
e.turn("left")
e.show_speed()
print(f"{e.name} color is {e.color}")

f = PoliceCar(70, "blue", "ford")
f.go()
f.show_speed()
print(f"{f.name} is police: {f.is_police}")
f.turn("right")
f.stop()
