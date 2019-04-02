from MyClasses import Dog


def average_age(dogs):
    return sum(d.age for d in dogs)/len(dogs)


def read_dogs_from_file():
    dogs = []
    with open("DogFile.csv") as dog_file:
        for line in dog_file:
            line = line.split(',')
            name = line[0].rstrip()
            breed = line[1].rstrip()
            age = int(line[2])
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

