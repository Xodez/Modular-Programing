'''
What if the name/age data holds each child's record
on the same line?
Ann,5
Fred,6
We read a line, split it into a list then put each
item from that list into the name and age lists.
'''
def read_data(name_of_file):
    connection = open(name_of_file)
    names_list = []
    ages_list = []
    while True:
        line = connection.readline()
        if line == "":
            break
        line_data = line.split(',')
        names_list.append(line_data[0])
        ages_list.append(int(line_data[1]))
    return names_list, ages_list


def main():
    filename = "kids_one_line.txt"
    names, ages = read_data(filename)
    print(names)
    print(ages)

main()