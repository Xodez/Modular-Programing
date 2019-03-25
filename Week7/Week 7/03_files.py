'''
This time the numbers are on one line, each
separated by comma
'''
def read_data(name_of_file):
    connection = open(name_of_file)
    # get the line of comma separated numbers
    line = connection.readline()
    # create a list out of this line of numbers
    data = line.split(',')
    # But this line creates strings e.g. '5'
    numbers = []
    for i in range(len(data)):
        numbers.append(int(data[i]))
    return numbers


def main():
    filename = "numbers_one_line.txt"
    list_of_numbers = read_data(filename)
    print(list_of_numbers)


main()