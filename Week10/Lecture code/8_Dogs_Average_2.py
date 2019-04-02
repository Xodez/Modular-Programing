from MyClasses import Dog


def average_age(dogs):
    return sum(d.age for d in dogs)/len(dogs)


def main():
    # Lists of objects
    dogs = [Dog("Freddie", 5, "King Charles"), Dog("Mikey", 6, "Greyhound"), Dog("Ruby", 2, "Mongrel"), Dog("Esme", 4, "Lurcher")]
    print("The average age of the dogs is {}".format(average_age(dogs)))

main()

