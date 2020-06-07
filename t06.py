def my_islower(str_1):
    l_1 = list(str_1)
    lower = True
    for s_1 in l_1:
        if (ord(s_1) not in range(97, 122 + 1)) and (ord(s_1) != 32):
            lower = False
    return lower


def int_func(str_1):
    return chr(ord(str_1[0]) - 32) + str_1[1:]


in_str = "A"
while not my_islower(in_str):
    in_str = input("enter string in lowercase: ")
in_list = in_str.split()
new_str = ""
for s in in_list:
    new_str += int_func(s) + " "

print(new_str)
