def get_pairs(lst: list) -> list[tuple]:
    """Returns a list of tuples. Tuple = (element of lst, next element of lst)"""
    length = len(lst)
    ind = 0
    if length == 1:
        return
    else:
        output_list = []
        while ind != length - 1:
            if ind == length:
                break
            else:
                output_list.append((lst[ind], lst[ind+1]))
                ind += 1
    return output_list


if __name__ == "__main__":
    print(get_pairs([1, 2, 3, 8, 9]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))
    print(get_pairs([1]))

