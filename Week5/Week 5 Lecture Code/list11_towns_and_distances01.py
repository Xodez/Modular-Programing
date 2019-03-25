#   Name; towns_and_distances v1
#   Author: Helen Fagan
towns = []
distances =  []
NUMBER_OF_TOWNS = 4;
i = 0
while  i < NUMBER_OF_TOWNS:
    name = input("Enter the name of a town")
    distance = int(input("Enter the distance to the town"))
    towns.append(name);
    distances.append(distance)
    i = i +1

print(towns)
print(distances)


nums = [1,2,3, 4]
smallest = min(nums)
posOf4 = nums.index(4)
print(posOf4)

