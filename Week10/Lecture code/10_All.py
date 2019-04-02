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


def the_oldest_dogs(dogs):
    oldest = max(dog.age for dog in dogs)
    oldest_dogs = [dog for dog in dogs if dog.age == oldest]
    print()
    print("There are {} dogs who are the oldest at {} years of age:".format(len(oldest_dogs), oldest))
    for dog in oldest_dogs:
        print("\t", dog.name)



def main():
    # Lists of objects
    dogs = read_dogs_from_file()
    print_dogs(dogs)
    print()
    print("The average age of the dogs is {}".format(average_age(dogs)))
    print()
    the_oldest_dogs(dogs)


main()

