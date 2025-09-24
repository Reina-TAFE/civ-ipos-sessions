phrase = "Hello there! How are you today?"


def set_solution(line):
    split_line = list(line)
    chr_set = set(split_line)
    most_frequent = ('a', 0)
    for i in chr_set:
        if i.isalpha():
            most_frequent = (i, split_line.count(i)) \
                if split_line.count(i) > most_frequent[1] else most_frequent
    return most_frequent


def list_solution(line):
    # create list of letters from line, filtering out non-alpha characters
    split_line = [char for char in list(line) if char.isalpha()]
    # find char with max count using map of tuples of (char, .count(char))
    most_frequent = max(map(lambda char: (char, split_line.count(char)), split_line), key=lambda x: x[1])
    return most_frequent


def dict_solution(line):
    letter_dict = dict(map(lambda char: (char, list(line).count(char)), set(list(line))))
    most_frequent = max({char: count for char, count in letter_dict.items() if char.isalpha()}
                        , key=lambda x: letter_dict[x])
    return most_frequent, letter_dict[most_frequent]


print(f"set solution: {set_solution(phrase)}")
print(f"list solution: {list_solution(phrase)}")
print(f"dict solution: {dict_solution(phrase)}")