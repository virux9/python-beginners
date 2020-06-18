out_f = open("file_t01_out.txt", "w", encoding="utf-8")

while True:
    in_str = input("enter line(enter to quit) : ")
    if in_str == "":
        break
    out_f.write(in_str + "\n")

out_f.close()
