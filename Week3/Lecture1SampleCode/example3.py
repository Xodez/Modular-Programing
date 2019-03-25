# Using a main() function to implement mainline logic in one function.


def write_line():
    print("=" * 23)


def greet_user():
    write_line()
    print("Welcome to my program")
    write_line()


def say_goodbye():
    write_line()
    print("Goodbye from my program")
    write_line()


def main():
    greet_user()
    say_goodbye()


main()