sum_numbers = 0
is_running = True
while is_running:
    str_num = input("enter numbers / q to quit : ")
    # str_num = "1 2 3 4 q"
    list_num = str_num.split()

    for str_n in list_num:
        try:
            sum_numbers += int(str_n)
        except ValueError:
            is_running = False
    print(f"sum:{sum_numbers}")
