from sys import argv


def calc_salary(total_h, per_h, extra):
    return (total_h * per_h) + extra


script_name, str_total_hours, str_price_per_hour, str_price_extra = argv

try:
    total_hours = int(str_total_hours)
    price_per_hour = int(str_price_per_hour)
    price_extra = int(str_price_extra)
except ValueError:
    print("Arguments must be numbers!")
    exit()

if (total_hours < 0) or (price_per_hour < 0) or (price_extra < 0):
    print("Numbers must be >= 0")
    exit()

s = calc_salary(total_hours, price_per_hour, price_extra)
print(f"Salary: {s}")
