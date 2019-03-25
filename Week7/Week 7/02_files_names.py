'''
Example to demonstrate reading numbers from a file into a list
using readlines() which leaves the content as strings and include
the new line character.
'''
def read_data(name_of_file):
    new_list = []
    connection = open(name_of_file)
    lines = connection.readlines()
    return lines

def main():
    filename = "names.txt"
    list_of_names = read_data(filename)
    print(list_of_names)

main()