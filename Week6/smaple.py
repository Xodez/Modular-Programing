def welcome():
    print("~~~~~~~~~~")
    print("~Welcome!~")
    print("~~~~~~~~~~")


def getData():
    name = input("Whats your name")
    numOfPets = int(input("how many pets do you have"))
    return name, numOfPets


def getNames(numOfPets):
    pets = ""
    for i in range(numOfPets):
        nameOfPet = input("what is the name of the pet")
        pets = nameOfPet + " " + pets
    return pets


def displayDetails(name, pets):
    petList = pets.split(" ")
    numOfPets = len(petList)
    vowel = ['A', 'O', 'U', 'I', 'E']
    vowelCount = 0
    totalLenght = 0
    print(str(name) + " Has " + str(numOfPets) + "pets called:")
    for i in range(numOfPets - 1):
        print("\t" + petList[i])
        # print(petList[i][0].upper())
        if petList[i][0].upper() in vowel:
            vowelCount = vowelCount + 1
        totalLenght = totalLenght + len(petList[i])
    loops = len(petList)-1
    averageLen = totalLenght/ loops
    print(averageLen)
    print(vowelCount)

def main():
    welcome()
    name, numOfPets = getData()
    pets = getNames(numOfPets)
    displayDetails(name, pets)


main()
