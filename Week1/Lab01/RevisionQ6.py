#Name: Kasparas Skruibis

averageTracker = 0
numOfStudents = int(input("Enter The Number Of Students "))
gradeSpreadSheet = ""
resultOfStudent = ""
i = 0
numOfStudentsIn1 = 0
numOfStudentsIn2 = 0
numOfStudentsIn3 = 0
numOfStudentsIn4 = 0
numOfStudentsIn5 = 0
largestGrade = 0
largestGradeName = ""

while i < numOfStudents:
    levelOfCourse = input("Enter The Level Of The Student ")
    nameOfStudent = input("Enter Students Name ")
    gradeOfStudent = input("Enter Students Grade ")
    if int(gradeOfStudent) > largestGrade:
        largestGrade = int(gradeOfStudent)
        largestGradeName = nameOfStudent
    averageTracker += int(gradeOfStudent)
    if int(gradeOfStudent) >= 70:
        numOfStudentsIn1 += 1
        if levelOfCourse == 8:
            resultOfStudent = "H1"
        else :
            resultOfStudent = "DT"
    elif 60 <= int(gradeOfStudent) <= 69:
        numOfStudentsIn2 += 1
        if levelOfCourse == 7:
            resultOfStudent = "H21"
        else :
            resultOfStudent = "M1"
    elif 50 <= int(gradeOfStudent) <= 59:
        numOfStudentsIn3 += 1
        if levelOfCourse == 7:
            resultOfStudent = "H22"
        else :
            resultOfStudent = "M2"
    elif 40 <= int(gradeOfStudent) <= 49:
        numOfStudentsIn4 += 1
        resultOfStudent = "Pass"
    else :
        numOfStudentsIn5 += 1
        resultOfStudent = "Fail"
    gradeSpreadSheet += nameOfStudent + "\t" + resultOfStudent + "\n"
    i += 1

averageTotal = averageTracker / numOfStudents

stats = gradeSpreadSheet + "\n"
stats += "Average" + str(averageTotal)
stats += "\n" + "%70+:" + str(numOfStudentsIn1) + "\n" + "%60-69:" + str(numOfStudentsIn2) + "\n" + "%50-59:" + str(numOfStudentsIn3) + "\n" + "%40-49:" + str(numOfStudentsIn4) + "\n" + "%40-:" + str(numOfStudentsIn5) + "\n"
stats += "Largest Grade: " + largestGradeName + str(largestGrade)

with open("results.txt", "w+") as f:
    f.write(stats)