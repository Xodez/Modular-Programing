#   Name: figure_it_out
#   Desc:  whats the output ? run to check your answers
#   Author: Helen Fagan
nameslist1 = [ "Ted", "Fred", "Tom"]
nameslist2 = [ "Ed", "Len", "Bob"]
print(nameslist1[0])
print(nameslist2[-1])
all_names = nameslist1 + nameslist2
print(all_names[0:5:2])
if "Ed" in all_names:
    print("found Ed")
print(all_names[-1][0])
names = nameslist1[0] + nameslist2[0]
print(names)
other_names = nameslist1[1] + nameslist2[1]
for i in nameslist1:
    print(i)
for i in names:
    print(i)
print(len(nameslist1))
for x,n in enumerate(nameslist1):
    print(x)

