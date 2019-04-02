class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # A method which returns the decimal
    # equivalent of the Fraction object.
    def decimal(self):
        if self.denominator != 0:
            return self.numerator / self.denominator
        else:
            return None


def main():
    f = Fraction(3,4)
    # use the object's decimal() method
    print(f.decimal())


main()