numbers = [12, 5, 6323, 56, 2, 47, 4, 8, 3, 135, 0, 8, 8]
sum_numbers = 0

with open("file_t05_out.txt", "w") as f_obj:
    for num in numbers:
        print(f"{num} ", file=f_obj, end="")
        sum_numbers += num

print(f"Sum of numbers: {sum_numbers}")
