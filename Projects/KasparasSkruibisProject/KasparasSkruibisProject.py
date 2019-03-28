# Kasparas Skruibis


def load_data():
    dataLists = [[], [], [], [], []]
    i = 0
    with open('data.txt') as f:
        for i, line in enumerate(f):
            dataLists[i % 5].append(line.strip())
    return dataLists


def show_menu():
    loop = True
    dataLists = load_data()
    while loop:
        print(30 * "-", "MENU", 30 * "-")
        print("1. Show all employees")
        print("2. Choose a specific employee")
        print("3. Edit the salary of an employee")
        print("4. Menu Option 4")
        print("5. Menu Option 4")
        print("6. Menu Option 4")
        print("7. Menu Option 7")
        print("8. Exit")
        print(67 * "-")
        try:
            choice = int(input("Enter your choice [1-8]: "))
        except:
            choice = 'error'
        if choice == 1:
            print("Showing employees")
            for i in range(len(dataLists[1])):
                print("ID:", dataLists[0][i], "|", "Name:", dataLists[1][i], dataLists[2][i], "|", "Email:",
                      dataLists[3][i], "|", "Salary:", dataLists[4][i])
        elif choice == 2:
            x = input("Please put in the ID of the employee: ")
            y = dataLists[0].index(x)
            print("ID:", dataLists[0][y], "|", "Name:", dataLists[1][y], dataLists[2][y], "|", "Email:",
                  dataLists[3][y], "|", "Salary:", dataLists[4][y])
        elif choice == 3:
            x = input("Please put in the ID of the employee: ")
            y = dataLists[0].index(x)
            z = input("Please put in the new salary: ")
            dataLists[4][y] = z
        elif choice == 4:
            print("Menu 4 has been selected")
        elif choice == 5:
            print("Menu 5 has been selected")
        elif choice == 6:
            print("Menu 5 has been selected")
        elif choice == 7:
            print("Menu 5 has been selected")
        elif choice == 8:
            print("Menu 5 has been selected")
            loop = False
        else:
            print("Wrong option selection. Enter any key to try again..")


def save_data():
    dataList = load_data()
    newList = []
    for i in range(len(dataList[0])):
        x1 = dataList[0][i]
        x2 = dataList[1][i]
        x3 = dataList[2][i]
        x4 = dataList[3][i]
        x5 = dataList[4][i]
        newList.append(x1)
        newList.append(x2)
        newList.append(x3)
        newList.append(x4)
        newList.append(x5)
    with open('testFile.txt', 'w') as f:
        for i in range(len(newList)):
            f.write(newList[i] + '\n')



def main():
    show_menu()
    save_data()


main()
