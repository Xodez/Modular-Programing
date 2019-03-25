def read_nonempty_alphabetical_string(prompt):
    while True:
        s = input(prompt)
        s_with_no_spaces = s.replace(' ', '')
        if len(s_with_no_spaces) > 0 and s_with_no_spaces.isalpha():
            break
        else:
            print("Please type letters only")
    return s


def read_fullname():
    f = read_nonempty_alphabetical_string("Firstname >>> ")
    s = read_nonempty_alphabetical_string("Surname >>> ")
    return f, s


def read_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number >= 0:
                break
            else:
                print("Non-negative numbers please...")
        except ValueError:
            print("Must be numeric...")
    return number


def read_percentage_float(prompt):
    while True:
        try:
            number = float(input(prompt))
            if 0 <= number <= 100:
                break
            else:
                print("Values 0-100 please...")
        except ValueError:
            print("Must be numeric...")
    return number


def read_personal_details():
    firstname, surname = read_fullname()
    prompt = firstname+"'s Age >>> "
    age = read_positive_integer(prompt)
    prompt = firstname + "'s grade >>> "
    grade = read_percentage_float(prompt)
    return firstname, surname, age, grade


def display_personal_details(f,s,a,g):
    print("Name:  {} {}".format(f,s))
    print("Age:   {}".format(a))
    print("Grade: {:.0f}%".format(g))


def main():
    student_firstname, student_surname, student_age, student_grade = read_personal_details()
    display_personal_details(student_firstname, student_surname, student_age, student_grade)


main()