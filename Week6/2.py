def get_months_that_start_with(dataset, letter):
    goodMonths = ""
    x = 0
    for i in range(len(dataset)):
        if dataset[i][:1] == letter:
            goodMonths = str(goodMonths) +" "+ str(dataset[i])

        x = x + 1
    return goodMonths,x


def main():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    j_months = get_months_that_start_with(months, 'A')
    print(j_months)


main()

# name = "Joe"
# if name.startswith('J'):
#   print("yes"