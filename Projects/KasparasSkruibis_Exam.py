# Kasparas Skruibis Lab Exam Week 8

def printTitle():
    print("Sunway - Your way to the Sun")
    print("----------------------------")

def readDestination():
    destination = input("Please put in your destination: ")
    country = input("Please put in your country: ")
    return destination, country

def getFlightCostsSixMonths(months):
    costs = []
    for i in range (len(months)):
        x = months[i]
        costInput = input("Please put in the ammount it will cost in " + x + " ")
        costs.append(costInput)
    return costs

def display(destination, country, costs, months):
    minValue = min(costs)
    x = costs.index(minValue)
    print("Holiday Destination: ", destination, ",", country)
    print("The Lowest Flight is:", minValue, months[x])

def main():
    printTitle()
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    destination, country = readDestination()
    costs = getFlightCostsSixMonths(months)
    display(destination, country, costs, months)


main()