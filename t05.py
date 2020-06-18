from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


my_list = [el for el in range(100, 1000 + 1)]
print(reduce(my_func, my_list))
