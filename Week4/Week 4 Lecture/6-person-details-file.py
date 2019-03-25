def read_personal_details_from_file(data_file):
    firstname = data_file.readline().rstrip()
    surname = data_file.readline().rstrip()
    age = int(data_file.readline().rstrip())
    grade = int(data_file.readline().rstrip())
    return firstname, surname, age, grade


def display_personal_details(f,s,a,g):
    print("Name:  {} {}".format(f,s))
    print("Age:   {}".format(a))
    print("Grade: {:.0f}%".format(g))


# Used to get the file's name
def read_nonempty_string(prompt):
    while True:
        s = input(prompt)
        s_with_no_spaces = s.replace(' ', '')
        if len(s_with_no_spaces) > 0 :
            break
        else:
            print("Please type letters only")
    return s


def connect_to_file(filename):
    try:
        data_file = open(filename)
    except IOError:
        print("Sorry - no such file. ")
        exit()
    return data_file


def main():
    filename = read_nonempty_string("File name >>> ")
    data = connect_to_file(filename)

    student_firstname, student_surname, student_age, student_grade \
        = read_personal_details_from_file(data)

    display_personal_details(student_firstname, student_surname,
                             student_age, student_grade)
    data.close()

main()