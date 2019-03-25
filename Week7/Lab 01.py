def fileStuff(filename):
    fileContents = []
    fileToOpen = filename + ".txt"
    with open(fileToOpen) as f:
        fileContents = f.readlines()
        fileContents = [x.strip() for x in fileContents]
    fileLenght = len(fileContents)
    # print(fileContents, fileLenght)
    return fileContents, fileLenght


def sortList(fileContents):
    fileContents.sort()
    # print(fileContents)
    return fileContents


def upperCase(list):
    listUpper = []
    for i in range(len(list)):
        listUpper.append(list[i].upper())
    # print(listUpper)
    return listUpper


def selectedLetterWord(list, letter):
    wantedWords = []
    # letter = letter.upper
    for i in range(len(list)):
        if list[i][0] == letter:
            wantedWords.append(list[i])
        else:
            continue
    # print(wantedWords)
    return wantedWords


def deleteDoubles(list):
    newList = []
    for i in range(len(list)):
        if list[i] not in newList:
            newList.append(list[i])
        else:
            continue
    # print(newList)
    return newList


def fruitOrder(list):
    vegList = []
    stockNo = []
    for i in range(len(list)):
        temp = list[i].split(" ")
        vegList.append(temp[0])
        stockNo.append(temp[1])
    # print(vegList,stockNo)
    return vegList, stockNo


def loginTest(userList, passList):
    login = False
    username = input("username")
    password = input("password")
    for i in range(len(userList)):
        if username == userList[i] and password == passList[i]:
            login = True
        else:
            continue
    if login == False:
        loginAttempt = "Wrong Username or Password"
    else:
        loginAttempt = "welcome"
    return loginAttempt


def main():
    userList = ["fred123", "mike43", "oscar23"]
    passList = ["letmein", "waterf0rd", "1LovePython"]
    fileContents, fileLenght = fileStuff("data")
    sortedList = sortList(fileContents)
    sortedListUpperCase = upperCase(sortedList)
    selectedLetterWords = selectedLetterWord(sortedList, "B")
    noDoublesList = deleteDoubles(sortedList)
    vegList, stockNo = fruitOrder(fileContents)
    login = loginTest(userList, passList)
    print(login)


main()
