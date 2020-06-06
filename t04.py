words = input("Enter words:")

words_list = words.split()
for ind, val in enumerate(words_list, 1):
    print(ind, val[:10])
