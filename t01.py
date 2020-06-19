from time import sleep


class TrafficLight:
    def __init__(self):
        self.__list_colors = ["красный", "желтый", "зеленый"]
        self.__state_duration = [7, 2, 3]
        self.__current_color_index = 0
        self.__color = ""

    def running(self):
        self.__color = self.__list_colors[self.__current_color_index]
        print(self.__color)
        wait_time = self.__state_duration[self.__current_color_index]
        print(f"waiting: {wait_time} sec...")
        sleep(wait_time)
        self.__current_color_index += 1
        if self.__current_color_index > 2:
            self.__current_color_index = 0


tl = TrafficLight()
for i in range(0, 10):
    tl.running()
