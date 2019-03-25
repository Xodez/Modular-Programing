'''
This time the numbers are on one line, each
separated by comma
'''

def read_data(name_of_file):
    connection = open(name_of_file)
    # read the line of data
    line = connection.readline()
    # split the line into separate strings
    data = line.split(',')
    # convert each string into an integer
    new_list = [int(x) for x in data]
    return new_list


def main():
    filename = "numbers_one_line.txt"
    list_of_numbers = read_data(filename)
    print(list_of_numbers)


main()