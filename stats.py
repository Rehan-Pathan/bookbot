def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    counts = {}
    for char in text.lower():  # convert everything to lowercase
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for ch, count in char_dict.items():
        if ch.isalpha():  # only keep alphabetical characters
            sorted_list.append({"char": ch, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
