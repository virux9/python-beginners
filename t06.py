out_dic = {}

with open("file_t06.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        s_0 = line.split(":")
        discipline_name = s_0[0]
        s_1 = s_0[1].split()
        total_hours = 0
        for s in s_1:
            if s != "—" and s != "-":
                total_hours += int(s.split("(")[0])
        out_dic[discipline_name]=total_hours

print(out_dic)
