from MyClasses import Dog


def average_age(dogs):
    sum_of_ages = 0
    number_of_dogs = len(dogs)
    for d in dogs:
        sum_of_ages += d.age

    return sum_of_ages / number_of_dogs


def main():
    # Lists of objects
    dogs = [Dog("Freddie", 5, "King Charles"), Dog("Mikey", 6, "Greyhound"), Dog("Ruby", 2, "Mongrel"), Dog("Esme", 4, "Lurcher")]
    print("The average age of the dogs is {}".format(average_age(dogs)))

main()

