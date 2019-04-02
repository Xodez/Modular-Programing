class Dog:
    # Note the double underscores in the name of this method
    def __init__(self, name, age, breed):
        self.name = name    # create a new field belonging to the class called name
        self.age = age      # create a new field called age
        self.breed = breed  # create a new field called breed

    def __str__(self):
         return "{} is a {} and is {} years old.".format(self.name, self.breed, self.age)


def main():
    # Instantiate the Dog object
    dog1 = Dog("Freddie", 5, "King Charles")
    dog2 = Dog("Mikey", 6, "Greyhound")
    print(dog1)
    print(dog2)

    # The same method can be used to write to a file
    dog_file = open("dogs.txt", "w")
    print(dog1, file=dog_file)
    print(dog2, file=dog_file)
    dog_file.close()

main()

