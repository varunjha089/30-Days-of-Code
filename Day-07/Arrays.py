def reverse_list(list):
    return [char for char in list[::-1]]


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    REVERSE_ARR = reverse_list(arr)

    FINAL = ''
    for i in range(len(REVERSE_ARR)):
        # print(i)
        FINAL += str(REVERSE_ARR[i])
        if i < n:
            FINAL += ' '
    print(FINAL)
