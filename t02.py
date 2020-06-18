def generator(in_list):
    for el in in_list:
        try:
            if el > prev_el:
                yield el
        except NameError:
            pass
        prev_el = el


g = generator([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])
my_list = []

for e in g:
    my_list.append(e)
print(my_list)
