def string_split(input_string, sep='.'):
    """ Returns list of substrings separated by sep """
    out = []
    index = 0
    if sep in input_string:
        while True:
            sep_index = input_string.find(sep, index)
            if sep_index == -1:
                out.append(input_string[index:])
                break
            out.append(input_string[index:sep_index])
            index = sep_index + 1
    else:
        return [input_string]
    return out


if __name__ == "__main__":
    print(string_split('Python. How much is there in this word!'))

