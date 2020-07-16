def print_table(NUMBER):
    for i in range(1, 11):
        print(str(NUMBER) + " x " + str(i) + " = " + str(NUMBER * i))


if __name__ == '__main__':
    n = int(input())
    print_table(n)
