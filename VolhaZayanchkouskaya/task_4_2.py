def check_palindrome(input_word):
    """ Returns a message: string of symbols are palindrome or not
        item - index of symbol from the beginning, opposite_item - from the end."""

    item = 0
    opposite_item = len(input_word) - 1
    is_palindrome = True
    while item < opposite_item:
        if input_word[item] != input_word[opposite_item]:
            is_palindrome = False
        item += 1
        opposite_item -= 1
    if is_palindrome:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")


if __name__ == '__main__':
    in_str = input("Enter string of symbols: ")
    check_palindrome(in_str.lower())

