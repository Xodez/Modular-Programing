'''
Example to demonstrate:
1. writing contents of a list to a file
2. reading numbers from a file into a list
   if the numbers are each on separate lines
'''
def read_data(name_of_file):
    new_list = []
    connection = open(name_of_file)
    while True:
        line = connection.readline()
        if line == "":
            break
        x = int(line)
        new_list.append(x)
    return new_list


def write_to_file(numbers, filename):
    destination = open(filename, 'w')
    for i in range(len(numbers)):
        print(numbers[i], file=destination)
    destination.close()


def main():
    data_file = "numbers.txt"
    list_of_numbers = read_data(data_file)

    output_filename = "output.txt"
    write_to_file(list_of_numbers, output_filename )


main()