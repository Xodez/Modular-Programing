# This program demonstrates how writing a separate function for write_line(), we make
# the code easier to edit in the future.


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


greet_user()
say_goodbye()