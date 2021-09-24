import string


def test_1_1(*input_list):
    """ Returns characters that appear in all strings"""
    res = [] # list of dictionaries, where key-letter, value - count(letter)
    lst = [] # list of keys of dictionaries
    test_1 = [] # list of characters that appear in all strings
    for str in input_list:
        d = {letter: str.count(letter) for letter in str}
        res.append(d)
    for d in res:
        for key in d:
            lst.append(key)
    for i in lst:
        if lst.count(i) == len(res):
            if i not in test_1:
                test_1.append(i)
    return test_1


def test_1_2(*input_list):
    """ Returns characters that appear in at least one string"""
    res = []
    lst = []
    test_2 = []
    for str in input_list:
        d = {c: str.count(c) for c in set(str)}
        res.append(d)
    for dict in res:
        for key in dict:
            lst.append(key)
    for i in lst:
        if lst.count(i) >= 1:
            if i not in test_2:
                test_2.append(i)
    return test_2


def test_1_3(*input_list):
    """ Returns characters that appear at least in two strings"""
    res = []
    lst = []
    test_3 = []
    for str in input_list:
        d = {c: str.count(c) for c in set(str)}
        res.append(d)
    for dict in res:
        for key in dict:
            lst.append(key)
    for i in lst:
        if lst.count(i) >= 2:
            if i not in test_3:
                test_3.append(i)
    return test_3


def test_1_4(*input_list):
    """ Returns characters of alphabet, that were not used in any string"""
    res = []
    lst = []
    test_4 = []
    for str in input_list:
        d = {c: str.count(c) for c in set(str)}
        res.append(d)
    for dict in res:
        for key in dict:
            lst.append(key)
    for i in string.ascii_lowercase:
        if i not in lst:
            test_4.append(i)
    return test_4


if __name__ == "__main__":

    strings = ["hello", "world", "python", ]

    print(test_1_1(*strings))
    print(test_1_2(*strings))
    print(test_1_3(*strings))
    print(test_1_4(*strings))

