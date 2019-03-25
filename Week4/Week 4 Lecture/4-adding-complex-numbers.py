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


def add_complex_numbers(r1, i1, r2, i2):
    return r1 + r2, i1+i2


def main():
    real_part1, imaginary_part1 = get_complex_number()
    real_part2, imaginary_part2 = get_complex_number()
    real_total, imaginary_total = add_complex_numbers(real_part1, imaginary_part1, real_part2, imaginary_part2)
    print("  ", end="")
    write_complex_number(real_part1, imaginary_part1)
    print("+ ", end="")
    write_complex_number(real_part2, imaginary_part2)
    print("-"*20)
    write_complex_number(real_total, imaginary_total)


main()