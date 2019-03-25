#Name: Kasparas Skruibis

levelOfCourse = input("Enter The Level Of The Student ")
nameOfStudent = input("Enter Students Name ")
gradeOfStudent = input("Enter Students Grade ")
gradeSpreadSheet = 0
resultOfStudent = ""

if int(gradeOfStudent) >= 70:
    if levelOfCourse == 8:
        resultOfStudent = "H1"
    else :
        resultOfStudent = "DT"
elif 60 <= int(gradeOfStudent) <= 69:
    if levelOfCourse == 7:
        resultOfStudent = "H21"
    else :
        resultOfStudent = "M1"
elif 50 <= int(gradeOfStudent) <= 59:
    if levelOfCourse == 7:
        resultOfStudent = "H22"
    else :
        resultOfStudent = "M2"
elif 40 <= int(gradeOfStudent) <= 49:
    resultOfStudent = "Pass"
else :
    resultOfStudent = "Fail"

print(resultOfStudent)