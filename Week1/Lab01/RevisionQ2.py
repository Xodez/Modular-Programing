#Name: Kasparas Skruibis

nameOfStudent = input("Enter Students Name ")
gradeOfStudent = input("Enter Students Grade ")
gradeSpreadSheet = 0
resultOfStudent = ""

if int(gradeOfStudent) >= 70:
    resultOfStudent = "H1"
elif 60 <= int(gradeOfStudent) <= 69:
    resultOfStudent = "H21"
elif 50 <= int(gradeOfStudent) <= 59:
    resultOfStudent = "H22"
elif 40 <= int(gradeOfStudent) <= 49:
    resultOfStudent = "Pass"
else :
    resultOfStudent = "Fail"

print(resultOfStudent)




