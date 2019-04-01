# Kasparas Skruibis

import random as r


def load_data():
    dataLists = [[], [], [], [], []]
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
        print("6. Add bonus for employees")
        print("7. Generate a report for management")
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
            input("Press enter to continue")
        elif choice == 2:
            x = input("Please put in the ID of the employee: ")
            y = dataLists[0].index(x)
            print("ID:", dataLists[0][y], "|", "Name:", dataLists[1][y], dataLists[2][y], "|", "Email:",
                  dataLists[3][y], "|", "Salary:", dataLists[4][y])
            input("Press enter to continue")
        elif choice == 3:
            x = input("Please put in the ID of the employee: ")
            y = dataLists[0].index(x)
            z = input("Please put in the new salary: ")
            dataLists[4][y] = z
            input("Press enter to continue")
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
            input("Press enter to continue")
        elif choice == 5:
            x = input("Please enter the employee ID you wish to delete: ")
            y = dataLists[0].index(x)
            for i in range(len(dataLists)):
                del dataLists[i][y]
        elif choice == 6:
            x = float(input("Put in the % value for the end of year bonus: "))
            tempList = []
            for i in dataLists[4]:
                y = float(i) / x
                tempList.append(y)
            with open('EndOfYearBonus.txt', 'w') as f:
                for i in range(len(tempList)):
                    f.write(str(dataLists[0][i]))
                    f.write("\n")
                    f.write(str(dataLists[1][i]))
                    f.write("\n")
                    f.write(str(dataLists[2][i]))
                    f.write("\n")
                    f.write(str(tempList[i]))
                    f.write("\n")
            input("Press enter to continue")
        elif choice == 7:
            print("Generate a report for management")
            sum = 0
            for i in dataLists[4]:
                sum += (float(i))
            x = sum / float(len(dataLists[4]))
            y = max(dataLists[4])
            z = dataLists[4].index(y)
            print(30 * "-", "REPORT", 30 * "-")
            print("Average salary =", x)
            print("Largest Salary =", dataLists[0][z], dataLists[1][z], dataLists[2][z], y)
            print(30 * "-", "REPORT", 30 * "-")
            input("Press enter to continue")
        elif choice == 8:
            print("Quitting application")
            loop = False
        else:
            print("Wrong option selection. Enter any key to try again..")


def save_data(dataLists):
    newList = []
    for i in range(len(dataLists[0])):
        newList.append(dataLists[0][i])
        newList.append(dataLists[1][i])
        newList.append(dataLists[2][i])
        newList.append(dataLists[3][i])
        newList.append(dataLists[4][i])
    with open('data.txt', 'w') as f:
        for i in range(len(newList)):
            f.write(str(newList[i]))
            f.write("\n")


def main():
    show_menu(dataLists)
    save_data(dataLists)


main()
