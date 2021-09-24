def split_by_index(s: str, indexes: list[int]) -> list[str]:
    """ Returns a list of strings splits by indexes specified in indexes """
    output_list = []
    indexes.append(len(s))
    start = 0
    for item in indexes:
        if item > len(s):
            output_list.append(s[start:])
            break
        else:
            output_list.append(s[start:item])
            start = item
    return output_list


if __name__ == '__main__':
    print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
    print(split_by_index("no luck", [42]))

