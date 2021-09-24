def get_longest_word(s: str) -> str:
    """ Returns a longest word in a sentence"""
    s = s.split()
    return max(s, key=len)


if __name__ == '__main__':
    input_string = "Any pythonista like namespaces a lot."
    print(get_longest_word(input_string))
    input_string1 = "Python is simple and effective!"
    print(get_longest_word(input_string1))




