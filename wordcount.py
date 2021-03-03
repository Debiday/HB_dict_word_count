def make_letter_counts_dict(file):
    """Create a dictionary that checks how manty times a letter repeats"""
    dictionary = {}

    with open('twain.txt') as f:
        for line in f:
            line = line.strip().split(" ")
            for words in line:
                if words not in dictionary:
                    dictionary[words] = 1
                else:
                    dictionary[words] += 1
        return dictionary

def long_form(dictionary):
    """Changes the dictionary format to print one key value per line"""
    for i, j in dictionary.items():
        print(f"{i} {j}")

print(long_form(make_letter_counts_dict('twain.txt')))
