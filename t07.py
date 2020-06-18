def fact(num):
    ret_val = 1
    for val in range(1, num):
        ret_val *= val
        yield ret_val


n = 20
x = 0
for i in fact(n + 1):
    x += 1
    print(f"{x}! = {i}")
