# Kasparas Skruibis


def load_data():
    openData = open('data.txt', 'r')
    idList = []
    fnameList = []
    lnameList = []
    emailList = []
    salaryList = []
    while True:
        with openData as f:
            line = f.read()



def show_menu():
    print(30 * "-", "MENU", 30 * "-")
    print("1. Menu Option 1")
    print("2. Menu Option 2")
    print("3. Menu Option 3")
    print("4. Menu Option 4")
    print("5. Exit")
    print(67 * "-")
    loop = True

    while loop:
        try:
            choice = int(input("Enter your choice [1-5]: "))
        except:
            choice = 'error'
        if choice == 1:
            print("Menu 1 has been selected")
            loop = False
        elif choice == 2:
            print("Menu 2 has been selected")
            loop = False
        elif choice == 3:
            print("Menu 3 has been selected")
            loop = False
        elif choice == 4:
            print("Menu 4 has been selected")
            loop = False
        elif choice == 5:
            print("Menu 5 has been selected")
            loop = False
        else:
            print("Wrong option selection. Enter any key to try again..")


def save_data():
    print('Test3')


def main():
    load_data()
    show_menu()
    save_data()


main()
