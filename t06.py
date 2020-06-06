# data = [
#     (1, {"название": "компьютер", "цена": 20000, "количество": 5, "ед": "шт"}),
#     (2, {"название": "принтер", "цена": 6000, "количество": 2, "ед": "шт"}),
#     (3, {"название": "сканер", "цена": 2000, "количество": 7, "ед": "шт"}),
# ]

data = []
idx = 1
while True:
    name = input("название:")
    price = int(input("цена:"))
    num = int(input("количество:"))
    ed = input("ед:")
    m_tup = (idx, {"название": name, "цена": price, "количество": num, "ед": ed})
    data.append(m_tup)
    idx += 1
    more = ""
    while more != "y" and more != "n":
        more = input("хотите ввести еще один товар? (y/n) ")
    if more == "n":
        break

print(data)

l_name = []
l_price = []
l_num = []
l_ed = []
for val in data:
    l_name.append(val[1]["название"])
    l_price.append(val[1]["цена"])
    l_num.append(val[1]["количество"])
    l_ed.append(val[1]["ед"])
d_result1 = {"название": l_name, "цена": l_price, "количество": l_num, "ед": l_ed}

s_name = set()
s_price = set()
s_num = set()
s_ed = set()
for val in data:
    s_name.add(val[1]["название"])
    s_price.add(val[1]["цена"])
    s_num.add(val[1]["количество"])
    s_ed.add(val[1]["ед"])
d_result2 = {"название": list(s_name), "цена": list(s_price), "количество": list(s_num), "ед": list(s_ed)}

print("списком:")
print(d_result1)
print("уникальные:")
print(d_result2)
