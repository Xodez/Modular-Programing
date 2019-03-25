#   Name: list operations
#   Desc:  operations on lists
#   Author: Helen Fagan
results = [91, 55, 67, 91,45]
results.append(40)
print(results)
results.remove(55)
print(results)
results.sort()
print(results)
results.reverse()
print(results)

index1 = results.index(91)
index2 = results.index(67)
print("Position of " + str(91) + " is " + str(index1))
print("Position of " + str(67) + " is " + str(index2))
item1 = results.pop()
print("Popped last item: "  + str(item1))
print(results)
item2 = results.pop(2)
print("Popped item from index 2: " + str(item2))
print(results)
print("Number of occurences of  " + str(45) + " is ", results.count(45))
print(results)
print(min(results))