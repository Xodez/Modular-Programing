#  Name:  Strings and list
#  Desc:  Slicing Strings and Methods that can be used with Strings
#         Converting Strings to lists and vice versa
word1 = "Hawaii"
word2 = "Honolulu"
word2 = word1
print("Slicing works with Strings")
print(word1[0:2])
print(word1[-3:-1])
print("Iterate over a String")
for x in word1:
    print(x)
for i,letter in enumerate(word1):
    print(i, letter)
print("Check if a letter is contains in a String")
if 'H' in word1:
    print("contains H")
print("Strings are immutable")
#  word1[0] = 'K'   illegal
print("Some methods are similar to list methods")
pos = word1.index('w')
print("w is at position " + str(pos)  + " in " + word1)
number = word1.count('i')
print("There are "+ str(number) + " i's in" + word1)
