def double(data):
    return [n * 2 for n in data]

def get_short_names(months):
    return [month[0:3] for month in months]

def get_months_that_start_with(months, letter):
    return [month for month in months if month.startswith(letter)]

def main():
    numbers = [4,5,6,2,8,9]
    numbers_doubled = double(numbers)
    print(numbers_doubled)

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    abbrev_names = get_short_names(months)
    print(abbrev_names)

    j_months = get_months_that_start_with(months, 'J')
    print(j_months)



main()