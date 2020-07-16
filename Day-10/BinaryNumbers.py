import itertools


def decimal_to_binary(dec):
    decimal = int(dec)
    binary_number = bin(decimal)
    slicing_binary = str(binary_number)[2:]
    return slicing_binary


def convert_to_list(number):
    final_lists = []
    for i in number:
        final_lists.append(i)
    return final_lists


if __name__ == '__main__':
    n = int(input())
    result = decimal_to_binary(n)
    final_list = convert_to_list(result)
    z = [(x[0], len(list(x[1]))) for x in itertools.groupby(final_list)]
    print(max(z, key=lambda x:x[1])[1])
