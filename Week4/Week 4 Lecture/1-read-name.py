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


def main():
    firstname, surname = read_fullname()
    print(firstname,surname)


main()
