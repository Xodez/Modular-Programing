class Dog:
    # Note the double underscores in the name of this method
    def __init__(self, name, age, breed):
        self.name = name    # create a new field belonging to the class called name
        self.age = age      # create a new field called age
        self.breed = breed  # create a new field called breed

def main():
    # Instantiate the Dog object
    dog1 = Dog("Freddie", 5, "King Charles")
    dog2 = Dog("Mikey", 6, "Greyhound")
    print("{} is a {} and is {} years old".format(dog1.name, dog1.breed, dog1.age))
    print("{} is a {} and is {} years old".format(dog2.name, dog2.breed, dog2.age))


main()

