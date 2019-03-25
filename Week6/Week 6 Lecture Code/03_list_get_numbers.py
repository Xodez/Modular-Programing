#  Name: get_numbers
#  Desc: show how to return a list of numbers from a method
def get_numbers(amount):
    numbers = [0] * amount
    i = 0
    while ( i < amount):
        number  = int(input("Please enter number " + str(i+1)))
        numbers[i]  = number
        i = i + 1
    return numbers

def main():
    amount_required = int(input("How many numbers do you want to add to the list?"))
    numbers_list = get_numbers(amount_required)
    print(numbers_list)

main()

