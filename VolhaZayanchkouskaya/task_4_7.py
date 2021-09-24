def foo(input_list):
    """ Returns a list of product of all original list values
    except the value at the current index."""
    output_list = []
    mult = 1
    for value in input_list:
        mult *= value
    for index in range(len(input_list)):
            output_list.append(int(mult/input_list[index]))
    return output_list


if __name__ == "__main__":
    print(foo([1, 2, 3, 4, 5]))
    print(foo([3, 2, 1]))

