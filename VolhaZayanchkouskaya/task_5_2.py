"""
Implement a function which search for most common words in the file.
Use `data/lorem_ipsum.txt` file as a example.
 NOTE: Remember about dots, commas, capital letters etc.
"""


import string


def most_common_words(filepath, number_of_words=3):
    """Returns number_of words most common words in a file"""
    with open(filepath, 'r') as f:
        file = f.read().lower()
        spec_chr = string.punctuation + "\n\t-..."
        file = "".join([ch for ch in file if ch not in spec_chr])
        file = file.split()
        d = {word: file.count(word) for word in file}
        l = sorted(d, key=d.get, reverse=True)
        res =[]
        for index in range(len(l)):
            if index < number_of_words:
                res.append(l[index])
        return res


if __name__ == "__main__":
    f = "data/lorem_ipsum.txt"
    print(most_common_words(f))

