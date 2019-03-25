def draw_a_solid_line():
    print("+", 10 * "-", "+", sep="")


def draw_a_gappy_line():
    print("-",10*" ", "-", sep="")


def main():
    draw_a_solid_line()
    for k in range(3):
        draw_a_gappy_line()
    draw_a_solid_line()

main()