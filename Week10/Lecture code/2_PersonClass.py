class Person:
    def __init__(self, f, s, a):
        self.firstname = f
        self.lastname = s
        self.age = a

    def __str__(self):
        return "{} {} ({} years old)".format(self.firstname, self.lastname, self.age)

    def nextMilestoneAge(self):
        from math import ceil
        if self.age % 10 == 0:
            return self.age + 10
        else:
            return ceil(self.age/10) * 10

    def initials(self):
        return self.firstname[0]+'.'+self.lastname[0]+'.'


def main():
    m = Person("Minnie", "Mouse", 56)
    print(m, "has initials", m.initials())
    print("On your next 'big' birthday you will be {} years old".format(m.nextMilestoneAge()))

main()