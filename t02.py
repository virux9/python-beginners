num_lines = 0
num_words = 0
with open("file_t02.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        num_lines += 1
        str_words = line.split()
        print(f"line {num_lines} length: {len(line.split())}")
print(f"Total lines: {num_lines}")
