from MyClasses import Dog


def average_age(dogs):
    return sum(d.age for d in dogs)/len(dogs)


def read_dogs_from_file():
    dogs = []
    with open("DogFile.txt") as dog_file:
        while True:
            name = dog_file.readline().rstrip()
            if name == "":
                break
            breed = dog_file.readline().rstrip()
            age = int(dog_file.readline())
            dog = Dog(name, age, breed)
            dogs.append(dog)
    return dogs


def print_dogs(dogs):
    for dog in dogs:
        print(dog)


def main():
    # Lists of objects
    dogs = read_dogs_from_file()
    print_dogs(dogs)
    print("The average age of the dogs is {}".format(average_age(dogs)))


main()

