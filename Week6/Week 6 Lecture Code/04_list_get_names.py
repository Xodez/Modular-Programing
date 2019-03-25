#  Name: get_names
#  Desc:   create a list in a method and return it
def get_names():
    names = []
    add_another_name = True
    while (add_another_name):
        name  = input("Please enter a name: ")
        names.append(name)
        more = input("Would you like to enter another name y/n")
        if more != 'y' and more != 'Y':
            add_another_name = False
    return names

def main():
    names_list = get_names()
    print(names_list)

main()