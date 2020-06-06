# [7,5,3,3,2]
my_list = [7, 5, 3, 3, 2]
in_val = int(input("Enter value:"))
if my_list.count(in_val) > 0:
    my_list.insert(my_list.index(in_val),in_val)
else:
    my_list.insert(0,in_val)
print(my_list)
