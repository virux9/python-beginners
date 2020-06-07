def my_div(var_1, var_2):
    try:
        var_3 = var_1 / var_2
    except ZeroDivisionError:
        var_3 = None
    return var_3


v_1 = int(input("enter value1: "))
v_2 = int(input("enter value2: "))
v_3 = my_div(v_1, v_2)
if type(v_3) is None:
    print(f"value1 / value2 = {v_3}")
else:
    print("division by zero!")
