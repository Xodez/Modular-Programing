#   Name; towns_and_distances
#   Author: Helen Fagan
towns = ["Fermoy","Mallow", "Kinsale"]
distances =  [ 25, 30, 15]
towns2 = [] + towns
towns2.sort()
print(towns2)

for i,town in enumerate(towns2):
    print(str(i) + "." + " Distance to " + town + " is " + str(distances[i]))


