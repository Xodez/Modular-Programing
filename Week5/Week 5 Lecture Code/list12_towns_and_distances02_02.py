#   Name; towns_and_distances
#   Author: Helen Fagan
towns = ["Fermoy", "Mallow", "Kinsale"]
distances = [25, 30, 15]

total = sum(distances)
amount = len(distances)
if amount != 0:
    avg = total/amount
else:
    avg = 0

print("The average distance is  {:.2f}".format(avg) + ".")

# get the smallest value in distances
shortest = min(distances)
# find the index of that smallest value
i = distances.index(shortest)
# print the town in the smallest value
print("The closest town is " + towns[i] + ".")





