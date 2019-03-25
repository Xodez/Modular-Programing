#   Name: Adding_merging_and_slicing
#   Author: Helen Fagan
nums = [0]
nums = nums * 5
print(nums)

list1 = ["China", "South Korea"]
list2 = ["Japan", "Malaysia"]
list3 = list1 + list2
list3.append("Vietnam")
print(list3)

sports = ["soccer", "rugby", "hurling", "tennis", "squash", "badminton"]
raquetSports = sports[3:6]
print(raquetSports)

#Checking for membership of a sequence
if   "tennis" in raquetSports:
	print ("Tennis is a raquet Sport")
