my_list = []
num_elem = int(input("Enter number of elements:"))
i = 0
while i < num_elem:
    my_list.append(input(f"Enter element {i}:"))
    i += 1

ind = 0
while ind < len(my_list) - 1:
    a = my_list[ind]
    my_list[ind] = my_list[ind + 1]
    my_list[ind + 1] = a
    ind += 2

print(my_list)
