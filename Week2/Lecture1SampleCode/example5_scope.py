def draw_a_solid_line():
    number_of_spaces = 10
    edge_character = '+'    # different variable to that in gappy_line()
    print(edge_character, number_of_spaces * "-", edge_character, sep="")


def gappy_line():
    number_of_dashes = 10
    edge_character = "-"    # different variable to that in solid_line()
    print(edge_character, number_of_dashes*" ", edge_character, sep="")


def main():
    number_of_gappy_lines = 3
    draw_a_solid_line()
    for k in range(number_of_gappy_lines):
        gappy_line()
    draw_a_solid_line()


main()