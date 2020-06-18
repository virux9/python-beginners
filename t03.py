num_employees = 0
total_salary = 0
with open("file_t03.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        s = line.split()
        salary = float(s[1])
        total_salary += salary
        num_employees += 1
        if salary < 20000:
            print(f"Employee {s[0]} salary is <20k")

print(f"average salary:{total_salary / num_employees}")
