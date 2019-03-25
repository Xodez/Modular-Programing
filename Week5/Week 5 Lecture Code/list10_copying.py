#   Name: copying
#   Desc:  shallow and deep copies
#   Author: Helen Fagan
list1= [ 9, 8, 2, 1]
# second  reference to the same list
list2 = list1
list1[0] = 66
list2[1] = 88
print(list1)
print(list2)

# a new list with a copy of the contents
list3 = []
for i in list1:
    list3.append(i)
list1[0] = 77
list3[1] = 44
print(list1)
print(list3)

# fastest way -a new list with a copy of the contents
list4 = [] + list1