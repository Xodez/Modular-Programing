class Fraction:
    DIVIDE_SYMBOL = chr(247)

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def decimal(self):
        if self.denominator != 0:
            return self.numerator / self.denominator
        else:
            return None

    # When print() is given an object as a parameter, the address
    # of the object is displayed or if a __str__ method is available,
    # the returned string is displayed.
    def __str__(self):
        return "{}{}{}".format(self.numerator, self.DIVIDE_SYMBOL, self.denominator)


def main():
    # Create a Fraction object
    f = Fraction(3,4)

    print(f.__dict__)

    print("{}={}".format(f, f.decimal()))

main()