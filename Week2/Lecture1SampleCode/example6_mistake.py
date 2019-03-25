def read_name():
    name = input("What is your name?")


def main():
    name = read_name()
    print("Hello {}".format(name))


main()