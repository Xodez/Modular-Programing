#   Name; towns_and_distances02
#   Desc:  using append
#   Author: Helen Fagan
towns = ["Fermoy","Mallow", "Kinsale"]
distances =  [ 25, 30, 15]
total = 0
for i in distances:
    total += i

amount = len(distances)
if amount != 0:
    avg = total/amount
else:
    avg = 0

print("The average distance is  " + "{:.2f}".format(avg) + ".")
shortest = min(distances)
i = distances.index(shortest)
print("The closest town is  " + towns[i] + ".")







