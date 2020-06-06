my_list = [1, 1.2, True, "str", [1, 2], (1, 2), {1, 2}]

for ind, val in enumerate(my_list, 1):
    print(f"Element {ind}: {val} {type(val)}")
