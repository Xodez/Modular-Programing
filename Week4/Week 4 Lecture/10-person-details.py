from reading_from_user import read_nonempty_alphabetical_string
from reading_from_user import read_positive_integer
from reading_from_user import read_percentage_float


def read_fullname():
    f = read_nonempty_alphabetical_string("Firstname >>> ")
    s = read_nonempty_alphabetical_string("Surname >>> ")
    return f, s


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