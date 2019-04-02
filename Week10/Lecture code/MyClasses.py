class Dog:
    # Note the double underscores in the name of this method
    def __init__(self, name, age, breed):
        self.name = name    # create a new field belonging to the class called name
        self.age = age      # create a new field called age
        self.breed = breed  # create a new field called breed


    def __str__(self):
        if self.age == 1:
            return "{} is a {} and is a year old.".format(self.name, self.breed)
        else:
            return "{} is a {} and is {} years old.".format(self.name, self.breed, self.age)

    def age_in_human_years(self):
        DOG_TO_HUMAN_YEARS_CONVERSION_FACTOR = 7
        return self.age * DOG_TO_HUMAN_YEARS_CONVERSION_FACTOR


