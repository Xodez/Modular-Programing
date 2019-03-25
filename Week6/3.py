def get_over_fives(names, ages):
    nameList = ""
    ageList = ""
    for i in range(len(names)):
        if ages[i] < 6:
            nameList = str(nameList) + " " + str(names[i])
            ageList = str(ageList) + " " + str(ages[i])

    return nameList, ageList


def main():
    names = ["mary", "ann", "ben", "kate", "emily"]
    ages = [4, 7, 9, 2, 1]
    names_over_five, ages_over_fives = get_over_fives(names, ages)
    print(names_over_five)
    print(ages_over_fives)


main()
