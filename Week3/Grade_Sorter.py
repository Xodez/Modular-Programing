def fileNameAsk(fileName):
    while True:
        file = input("file name")
        if fileName == "":
            continue
        else:
            break
    return file


def grader(file):
    grade70 = 0
    grade60 = 0
    grade50 = 0
    grade40 = 0
    gradeFail = 0

    results = (file.readline().rstrip())
    if results <= 39:
        grade1 = "Fail"
        gradeFail = gradeFail + 1
    elif 40 <= results <= 49:
        grade2 = "Pass"
        grade40 = grade40 + 1
    elif 50 <= results <= 59:
        grade3 = "H22"
        grade50 = grade50 + 1
    elif 60 <= results <= 69:
        grade4 = "H21"
        grade60 = grade60 + 1
    elif results >= 70:
        grade5 = "H1"
        grade70 = grade70 + 1
