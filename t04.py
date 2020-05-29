n = int(input("input number: "))

max_digit = 0
while True:
    d = n * 0.1
    digit = int(d % 1 * 10)
    if digit == 9:
        max_digit = digit
        break
    if digit > max_digit:
        max_digit = digit
    n = d // 1
    if n == 0.0:
        break

print(f"max_digit: {max_digit}")
