my_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("file_t04.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        s = line.split()
        f_w = open("file_t04_out.txt", "a", encoding="utf-8")
        f_w.write(f"{my_dic[s[0]]} - {s[2]}\n")
        f_w.close()
