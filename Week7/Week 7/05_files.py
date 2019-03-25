'''
What if each line has a separate piece of data:
Ann
5
Fred
6
where Ann is a name, and 5 is the age etc.
We must read the first line as a string, the second
as an integer, then a string etc.
'''
def read_data(name_of_file):
    connection = open(name_of_file)
    # create empty lists
    names_list = []
    ages_list = []
    while True:
        # get the first line
        line = connection.readline().rstrip()
        if line == "":
            break
        # append the first line to the names_list
        names_list.append(line)
        # get the next line
        line = connection.readline().rstrip()
        # convert hte next line to an integer and
        # append to the list
        ages_list.append(int(line))
    return names_list, ages_list


def main():
    filename = "kids.txt"
    names, ages = read_data(filename)
    print(names)
    print(ages)

main()