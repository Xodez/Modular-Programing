# Sample Exam Kasparas Skruibis

def welcome():
    print("======")
    print("Welcome")
    print("======")

def get_data():
    name = input("What is your name ")
    numberOfPets = int(input("How much pets "))
    return name, numberOfPets

def get_names(numberOfPets):
    pets = []
    for i in range (numberOfPets):
        nameOfPet = input("What is the name fo your pet ")
        pets.append(nameOfPet)
    print(pets)
    return pets

def display_details(name, pets):
    print(name, "has", len(pets), "called:" )
    for i in range (len(pets)):
        print(pets[i])

def main():
    welcome()
    name, numberOfPets = get_data()
    pets = get_names(numberOfPets)
    display_details(name, pets)

main()


