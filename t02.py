class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if b == 0:
        raise OwnError("Error: Division by zero!")
    c = a / b
except ValueError:
    print("Error: Must be a number!")
except OwnError as err:
    print(err)
else:
    print(f"a / b = {c}")
finally:
    print("Program ended.")
