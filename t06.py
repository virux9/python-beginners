a = int(input("a:"))
b = int(input("b:"))
day0 = a
d = 1
while day0 < b:
    day0 = day0 + (day0 * 0.1)
    d += 1

print(f"На {d}-й день спортсмен достиг результата — не менее {b} км")
