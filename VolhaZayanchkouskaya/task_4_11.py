def combine_dicts(*args):
    """Returns dictionary with sum of values the same keys"""
    res = {}
    for item in args:
        for key in item:
            if key in res:
                res[key] += item[key]
            else:
                res[key] = item[key]
    return res


if __name__ == '__main__':
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}
    print(combine_dicts(dict_1, dict_2))
    print(combine_dicts(dict_1, dict_2, dict_3))
