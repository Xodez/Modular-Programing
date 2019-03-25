# The parameter becomes the type of its corresponding argument.


def sing(name):
    print("name is a {}".format(type(name)))
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print("Happy Birthday dear", name)
    print("Happy Birthday to you!")
    print()


def main():
    sing("Fred")        # The parameter name becomes a string with the value "Fred"
    sing("Matilda")     # The parameter name becomes a string with the value "Matilda"

    sing(5.6)           # The parameter name becomes a float with the value 5.6

main()

