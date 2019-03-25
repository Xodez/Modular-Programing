#   Name: list04_creation.py
#   Author: Helen Fagan
numsList = [0]
numsList = numsList * 5
print("numsList is " + str(numsList))
smallList = [1,2,3]
bigList = smallList * 5
print("bigList is " + str(bigList) )
bigList[6:11] = numsList
print("bigList is " + str(bigList) )
