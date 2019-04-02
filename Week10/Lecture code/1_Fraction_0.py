class Fraction:
    # Fraction is a class - a composite data type
    # containing functions (methods) and data.
    # When an object is created from a class,
    # the initialisation method is called and it
    # creates and populates the fields (data attributes)
    # of the object
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


def main():
    # Create a Fraction object
    f = Fraction(3,4)

    # displays the structure of the object
    print(f.__dict__)

    # accessing fields using .
    print(f.numerator)
    print(f.denominator)


main()