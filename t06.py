from itertools import count, cycle

start_number = int(input("Enter start number: "))
for num in count(start_number):
    print(num)
    if input("enter=next, q=quit ") == "q":
        break

my_list = input("Enter elements: ").split()
for el in cycle(my_list):
    print(el)
    if input("enter=next, q=quit ") == "q":
        break
