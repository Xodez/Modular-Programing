import random as r


def loadListFromFile(filename):
    fileContents = []
    fileToOpen = filename + ".txt"
    with open(fileToOpen) as f:
        fileContents = f.readlines()
        fileContents = [x.strip() for x in fileContents]
    countries = []
    capitals = []
    for i in range(len(fileContents)):
        temp = fileContents[i].split(", ")
        countries.append(temp[0])
        capitals.append(temp[1])
    return countries, capitals


def askCapital(countries, capitals, numer, loops):
    answer = countries[numer].upper()
    # print(answer)
    # question = answer
    points = False
    question = input(str(loops) + ". In what country is " + capitals[numer] + " ?").upper()
    if question == answer:
        points = True
    else:
        points = False
    return points


def askCountry(countries, capitals, number, loops):
    answer = capitals[number].upper()
    # print(answer)
    # question = answer
    points = False
    question = input(str(loops) + ". What is the capital of " + countries[number] + " ?").upper()
    if question == answer:
        points = True
    else:
        points = False
    return points


def run_quiz(countries, capitals):
    questionAsked = []
    loops = 1
    answer = 0
    running = True
    while running == True:
        questionNumber = r.randint(0, (len(countries) - 1))
        if questionNumber in questionAsked:
            continue
        else:
            questionAsked.append(questionNumber)
        questionType = r.randint(1, 2)
        if questionType == 1:
            result = askCapital(countries, capitals, questionNumber, loops)
            loops = loops + 1
            if result == True:
                answer = answer + 1
        elif questionType == 2:
            result = askCountry(countries, capitals, questionNumber, loops)
            loops = loops + 1
            if result == True:
                answer = answer + 1
        if loops == (len(countries) + 1):
            running = False
    return answer


def main():
    countries, capitals = loadListFromFile("countries")
    score = run_quiz(countries, capitals)
    print("you answered " + str(score) + " correctly out of " + str(len(countries)) + "!")


main()
