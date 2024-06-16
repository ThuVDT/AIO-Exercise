# !gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
# file_path = "/content/P1_data.txt"

def standardlize(data):
    data = data.lower()
    data = data.split()
    return data


def sort_dict_by_key(dict_input):
    sort_keys = sorted(dict_input.keys())
    final_dict = {}
    for key in sort_keys:
        final_dict[key] = dict_input[key]
    return final_dict


def word_count(file_path):
    file = open(file_path, "r")
    data = file.read()
    file.close()

    data = standardlize(data)
    word_dict = {}
    for i in range(len(data)):
        if word_dict.get(data[i]) == None:
            word_dict.setdefault(data[i], 1)
        else:
            word_dict[data[i]] += 1
    print(sort_dict_by_key(word_dict))

# word_count(file_path)
