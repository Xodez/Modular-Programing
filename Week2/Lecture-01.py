# #
# def printBanner():
#     print("===========")
#     print("  Welcome")
#     print("===========")
#
# printBanner()
# #
# #
# def greetUser():
#     print("=" * 23)
#     print("Welcome")
#     print("=" * 23)
#
# def main():
#     greetUser()
#
# main()
# #
#
def spaggetiLong():
    lenght = 10

    print("+", "-" * lenght, "+")


def spaggetiTall():
    lenght = 10
    print("-", " " * lenght, "-")


def main():
    spaggetiLong()
    tall = 5
    loops = 1
    while tall >= loops:
        loops = loops + 1
        spaggetiTall()
    spaggetiLong()

main()
#