def print_line(number, character):
    print(character * number)


def print_file():
    file = open("debug_text.txt")
    for line in file:
        for character in line:
            if character.isupper():
                print_line(5, character)


def main():
    print_file()


main()