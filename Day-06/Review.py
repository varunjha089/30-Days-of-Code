def string_arrangement(string):
    str_one = ''
    str_two = ''

    for i in range(len(string)):
        if i % 2 != 0:
            str_two += string[i]
        else:
            str_one += string[i]

    return str_one + " " + str_two


if __name__ == "__main__":
    NO_OF_LOOP = int(input())
    for i in range(NO_OF_LOOP):
        STRING_INPUT = str(input())
        VALUE = string_arrangement(STRING_INPUT)
        print(VALUE)
