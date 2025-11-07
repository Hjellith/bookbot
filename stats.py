def word_count(path):
    with open(path) as f:
        text = f.read()
    return len(text.split())

def get_num_characters(path):
    with open(path) as f:
        text = f.read().lower()
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(items):
    return items["num"]

def sort_counts(dict_count):
    count_list = []
    new_dict = {}
    for key, value in dict_count.items():
        new_dict["char"] = key
        new_dict["num"] = value
        if new_dict["char"].isalpha():
            count_list.append(new_dict.copy())
    count_list.sort(reverse=True, key=sort_on)
    return count_list
