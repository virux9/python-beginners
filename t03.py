class OwnTextError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        inp_str = input("Enter number or 'stop' to quit :")
        if not inp_str.isnumeric():
            if inp_str == "stop":
                exit()
            else:
                raise OwnTextError("Not a number!")
    except OwnTextError as err:
        print(err)
    else:
        my_list.append(int(inp_str))
    finally:
        print(my_list)
