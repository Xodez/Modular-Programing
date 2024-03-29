# Kasparas Skruibis

import random as r


# Loads the data onto lists
def loadData():
    try:
        dataLists = [[], [], [], [], []]
        with open('employee.txt') as f:
            for i, line in enumerate(f):
                dataLists[i % 5].append(line.strip())
        return dataLists
    except:
        print("Something went wrong loading the file: ")


dataLists = loadData()


# Shows all employees
def showAllEmployees(dataLists):
    print("Showing employees")
    for i in range(len(dataLists[1])):
        print("ID:", dataLists[0][i], "|", "Name:", dataLists[1][i], dataLists[2][i], "|", "Email:",
              dataLists[3][i], "|", "Salary:", dataLists[4][i])
    input("Press enter to continue")


# shows specific employee
def chooseSpecificEmployee(dataLists):
    while True:
        x = input("Please put in the ID of the employee: ")
        if x in dataLists[0]:
            break
        else:
            print("Invalid Input")
    y = dataLists[0].index(x)
    print("ID:", dataLists[0][y], "|", "Name:", dataLists[1][y], dataLists[2][y], "|", "Email:",
          dataLists[3][y], "|", "Salary:", dataLists[4][y])
    input("Press enter to continue")


# Edits employee salary
def editSalary(dataLists):
    while True:
        x = input("Please put in the ID of the employee: ")
        if x in dataLists[0]:
            break
        else:
            print("Invalid Input")
    y = dataLists[0].index(x)
    print("Current salary:", dataLists[4][y])
    while True:
        z = input("Please put in the new salary: ")
        try:
            val = float(z)
            pass
        except:
            print("The input must be a number")
            continue
        if z == "":
            print("Input cannon be empty")
        else:
            break
    dataLists[4][y] = z
    input("Press enter to continue")


# Add an employee
def addEmployee(dataLists):
    while True:
        x = input("Please put in the first name of the employee: ")
        try:
            val = int(x)
            print("The input cannot be a number")
            continue
        except:
            pass
        if x == "":
            print("Input cannon be empty")
        elif len(x) > 12:
            print("The input cannot be over 12 characters long")
        else:
            break
    while True:
        y = input("Please put in the last name of the employee: ")
        try:
            val = int(y)
            print("The input cannot be a number")
            continue
        except:
            pass
        if y == "":
            print("Input cannon be empty")
        elif len(y) > 12:
            print("The input cannot be over 12 characters long")
        else:
            break
    while True:
        z = input("Please put in the salary of the employee: ")
        try:
            val = float(z)
            pass
        except:
            print("The input must be a number")
            continue
        if z == "":
            print("Input cannon be empty")
        elif len(z) > 12:
            print("The input cannot be over 12 characters long")
        else:
            break
    while True:
        genID = r.randint(10000, 99999)
        if genID in dataLists[0]:
            continue
        else:
            break
    email = x + y + str(genID) + "@gmail.com"
    dataLists[0].append(str(genID))
    dataLists[1].append(str(x))
    dataLists[2].append(str(y))
    dataLists[3].append(str(email))
    dataLists[4].append(str(z))
    input("Press enter to continue")


# Remove employee
def removeEmployee(dataLists):
    while True:
        x = input("Please enter the employee ID you wish to delete: ")
        if x in dataLists[0]:
            break
        else:
            print("Id not in file")
    y = dataLists[0].index(x)
    for i in range(len(dataLists)):
        del dataLists[i][y]
    input("Press enter to continue")


# Make the bonus sheet file
def addBonus(dataLists):
    while True:
        x = input("Put in the % of the bonus: ")
        try:
            val = float(x)
            break
        except:
            print("The input must be a %")
    xFloat = float(x)
    tempList = []
    for i in dataLists[4]:
        y = float(i) / xFloat
        y_r = round(float(y), 2)
        y_str = str(y_r)
        tempList.append(y_str)
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


# Generate report
def genReport(dataLists):
    print("Generating a report for management")
    sum = 0
    for i in dataLists[4]:
        sum += (float(i))
    x = sum / float(len(dataLists[4]))
    y = max(dataLists[4])
    z = dataLists[4].index(y)
    print(30 * "-", "REPORT", 30 * "-")
    print("Average salary =", x)
    print("Largest Salary =", "ID:", dataLists[0][z], "Name:", dataLists[1][z], dataLists[2][z], "Salary:", y)
    print(30 * "-", "REPORT", 30 * "-")
    input("Press enter to continue")


# Quit and save
def quitAndSave():
    x = input("Would you like to save and quit? y/n: ")
    if x == "y" or x == "yes":
        print("Saving data")
        saveData(dataLists)
    print("Quitting application")


# This is the menu function, it will ask the user what it wants and contains all code to execute the input of the user.
def showMenu(dataLists):
    # This is the menu. It will show the user the options that s/he has.
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
        print(30 * "-", "MENU", 30 * "-")
        try:
            choice = int(input("Enter your choice [1-8]: "))
        except:
            choice = 'error'
        # This is all the code for the different options that the user can chose.
        if choice == 1:
            showAllEmployees(dataLists)
        elif choice == 2:
            chooseSpecificEmployee(dataLists)
        elif choice == 3:
            editSalary(dataLists)
        elif choice == 4:
            addEmployee(dataLists)
        elif choice == 5:
            removeEmployee(dataLists)
        elif choice == 6:
            addBonus(dataLists)
        elif choice == 7:
            genReport(dataLists)
        elif choice == 8:
            quitAndSave()
            loop = False
        else:
            input("Incorrect option. Press the enter key to try again..")


# This is the save function. When it is called it will save all data onto the text files.
def saveData(dataLists):
    newList = []
    for i in range(len(dataLists[0])):
        newList.append(dataLists[0][i])
        newList.append(dataLists[1][i])
        newList.append(dataLists[2][i])
        newList.append(dataLists[3][i])
        newList.append(dataLists[4][i])
    with open('employee.txt', 'w') as f:
        for i in range(len(newList)):
            f.write(str(newList[i]))
            f.write("\n")


# This main function runs the program
def main():
    showMenu(dataLists)


main()
