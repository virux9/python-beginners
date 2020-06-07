def my_func(x, y):
    y = abs(y)
    x_res = x
    for i in range(0, y - 1):
        x_res *= x
    return 1 / x_res


val_1 = 0
while val_1 <= 0:
    val_1 = float(input("enter x > 0, float : "))
val_2 = 0
while val_2 >= 0:
    val_2 = int(input("enter y < 0, int : "))

print(val_1 ** val_2)
print(my_func(val_1, val_2))
