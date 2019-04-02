class Dog:
    def __init__(self, name, age, breed):
        self.name = name    # create a new field belonging to the class called name
        self.age = age      # create a new field called age
        self.breed = breed  # create a new field called breed

    def __str__(self):
        if self.age == 1:
            return "{} is a {} and is a year old.".format(self.name, self.breed)
        else:
            return "{} is a {} and is {} years old.".format(self.name, self.breed, self.age)


def main():
    dog1 = Dog("Freddie", 5, "King Charles")
    dog2 = Dog("Mikey", 6, "Greyhound")
    print(dog1)
    print(dog2)
    print()
    # add 1 to the dogs' ages
    dog1.age += 1
    dog2.age += 1
    print(dog1)
    print(dog2)


main()

