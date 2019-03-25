NUMBER_OF_TOWNS = 4
towns = [None]*NUMBER_OF_TOWNS
distances =  [None]*NUMBER_OF_TOWNS

i = 0
while  i < NUMBER_OF_TOWNS:
    name = input("Enter the name of a town")
    distance = int(input("Enter the distance to the town"))
    towns[i] = name
    distances[i] = distance
    i = i +1

print(towns)
print(distances)




