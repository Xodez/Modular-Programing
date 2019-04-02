DIVIDE_SYMBOL = chr(247)

def decimal(x, y):
    if y != 0:
        return x/y
    else:
        return None


def display_fraction(x,y):
    print("{}{}{}".format(x, DIVIDE_SYMBOL, y), end="")


def main():
    numerator = 3
    denominator = 4
    display_fraction(numerator,denominator)
    print( ' =', decimal(numerator,denominator) )

main()