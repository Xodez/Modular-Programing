def read_float(prompt):
    while True:
        try:
            number = float(input(prompt))
            break
        except ValueError:
            print("Must be numeric...")
    return number


def get_complex_number():
    real = read_float("Real part >>> ")
    imaginary = read_float("Imaginary part >>> ")
    return real, imaginary


def write_complex_number(r, i):
    print("{:.4f}{:+.4f}i".format(r, i))


def main():
    real_part, imaginary_part = get_complex_number()
    write_complex_number(real_part, imaginary_part)


main()