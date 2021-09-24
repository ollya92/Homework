def replace_characters(input_str):
    """Returns a string with replaced symbols " with ' and vise versa """
    output_str = input_str.replace("\"", "+").replace("\'", "\"").replace("+", "\'")
    return output_str


if __name__ == '__main__':
    print(replace_characters("dfksdjfhk\'\'\'djfkbk\"\"fghfhdhjbvhjdh\""))

