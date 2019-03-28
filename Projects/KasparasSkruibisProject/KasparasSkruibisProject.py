# Kasparas Skruibis

import random as r


def load_data():
    dataLists = [[], [], [], [], []]
    i = 0
    with open('data.txt') as f:
        for i, line in enumerate(f):
            dataLists[i % 5].append(line.strip())
    return dataLists


dataLists = load_data()


def show_menu(dataLists):
    loop = True
    while loop:
        print(30 * "-", "MENU", 30 * "-")
        print("1. Show all employees")
        print("2. Choose a specific employee")
        print("3. Edit the salary of an employee")
        print("4. Add employee")
        print("5. Remove employee")
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
            x = input("Please put in the first name of the employee: ")
            y = input("Please put in the last name of the employee: ")
            z = input("Please put in the salary of the employee: ")
            genID = r.randint(10000, 99999)
            email = x + y + "@gmail.com"
            dataLists[0].append(genID)
            dataLists[1].append(x)
            dataLists[2].append(y)
            dataLists[3].append(email)
            dataLists[4].append(z)
        elif choice == 5:
            x = input("Please enter the employee ID you wish to delete: ")
            y = dataLists[0].index(x)
            for i in range(len(dataLists)):
                del dataLists[i][y]
        elif choice == 6:
            print("Menu 5 has been selected")
        elif choice == 7:
            print("Menu 5 has been selected")
        elif choice == 8:
            print("Menu 5 has been selected")
            loop = False
        else:
            print("Wrong option selection. Enter any key to try again..")


def save_data(dataLists):
    newList = []
    for i in range(len(dataLists[0])):
        x1 = dataLists[0][i]
        x2 = dataLists[1][i]
        x3 = dataLists[2][i]
        x4 = dataLists[3][i]
        x5 = dataLists[4][i]
        newList.append(x1)
        newList.append(x2)
        newList.append(x3)
        newList.append(x4)
        newList.append(x5)
    with open('data.txt', 'w') as f:
        for i in range(len(newList)):
            f.write(str(newList[i]))
            f.write("\n")


def main():
    show_menu(dataLists)
    save_data(dataLists)


main()
