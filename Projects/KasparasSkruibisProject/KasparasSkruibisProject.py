# Kasparas Skruibis


def load_data():
    dataLists = [[], [], [], [], []]
    i = 0
    with open('data.txt') as f:
        for i, line in enumerate(f):
            dataLists[i % 5].append(line.strip())
    return dataLists


def show_menu():
    print(30 * "-", "MENU", 30 * "-")
    print("1. Show all employees")
    print("2. Menu Option 2")
    print("3. Menu Option 3")
    print("4. Menu Option 4")
    print("5. Exit")
    print(67 * "-")
    loop = True
    dataLists = load_data()
    while loop:
        try:
            choice = int(input("Enter your choice [1-5]: "))
        except:
            choice = 'error'
        if choice == 1:
            print("Showing employees")
            for i in range(len(dataLists[1])):
                print("ID:", dataLists[0][i], "|", "Name:", dataLists[1][i], dataLists[2][i], "|", "Email:",
                      dataLists[3][i], "|", "Salary:", dataLists[4][i])
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
    show_menu()
    save_data()


main()
