if __name__ == "__main__":
    DICTIONARY = {}
    NO_OF_ENTRY = int(input())
    for i in range(NO_OF_ENTRY):
        NAME, VALUE = input().split()
        DICTIONARY[NAME] = VALUE

    for i in range(NO_OF_ENTRY):
        SEARCH_NAME = input()
        if SEARCH_NAME in DICTIONARY:
            print("%s=%s" % (SEARCH_NAME, DICTIONARY[SEARCH_NAME]))
        else:
            print("Not found")
