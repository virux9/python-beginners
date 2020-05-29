in_sec = int(input("enter seconds:"))
min_total = in_sec // 60
sec = in_sec % 60
hours = min_total // 60
minutes = min_total % 60

print(f"{hours:02}:{minutes:02}:{sec:02}")
