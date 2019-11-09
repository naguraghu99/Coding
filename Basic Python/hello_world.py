# First program


def hello_word(name):
    print('Hello ', name)


def main():
    hello_word('nagu')


    list1 = []
    list2 = []
    list3 = list1

    if (list1 == list2):
        print("1 True")
    else:
        print("1 False")

    if (list1 is list2):
        print("2 True")
    else:
        print("2 False")

    if (list1 is list3):
        print("3 True")
    else:
        print("3 False")


if __name__ == "__main__":
    main()
