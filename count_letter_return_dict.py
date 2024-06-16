def count_chars(string):
    char_dict = {}
    for i in range(len(string)):
        if char_dict.get(string[i]) == None:
            char_dict.setdefault(string[i], 1)
        else:
            char_dict[string[i]] += 1
    print(char_dict)


string = input("String: ")
count_chars(string)
