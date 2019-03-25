'''
Example to demonstrate reading numbers from a file into a list.
Each number is on a separate line.
readlines() creates a list of lines from the file.
List comprehension statement to create a new list in which
each line is converted from a string to an integer and appended to the list
'''
def read_data(name_of_file):
    connection = open(name_of_file)
    lines = connection.readlines()
    numbers = [int(line) for line in lines]
    return numbers

def main():
    filename = "numbers.txt"
    list_of_numbers = read_data(filename)
    print(list_of_numbers)

main()