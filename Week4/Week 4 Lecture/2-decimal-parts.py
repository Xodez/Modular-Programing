def read_float(prompt):
    while True:
        try:
            number = float(input(prompt))
            break
        except ValueError:
            print("Must be numeric...")
    return number


def find_parts(x):
    integer = int(x)
    decimal = x - integer
    return integer, decimal


def main():
    number = read_float("Decimal number >>> ")
    whole, decimal_part = find_parts(number)
    print("The whole part is", whole)
    print("The decimal part is", format(decimal_part,'.6f'))


main()
