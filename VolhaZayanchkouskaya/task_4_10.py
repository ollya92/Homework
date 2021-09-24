def generate_squares(num):
    """ Returns a dictionary where key is a number of range [1;num] and
    value is a square of key"""
    output = {}
    for key in range(1, num+1):
        output[key] = key ** 2
    return output


if __name__ == '__main__':
    print(generate_squares(5))

