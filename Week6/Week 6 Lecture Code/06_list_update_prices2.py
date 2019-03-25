#  Name: show_names
#  Desc:   create a new list and  use it to store updated prices
#          use for loop or list comprehension short cut.
def  half_prices(list):
    new_prices = []
    for item in list:
        new_prices.append(item/2)
    return (new_prices)

def  half_prices2(list):
    new_prices = []
    # shorter way to do the same thing as for loop above
    new_prices = [item * .5 for item in list]
    return (new_prices)

def main():
    list = [ 40.00, 30.50, 1.10, 99.00]
    print(list)
    print("create a new list to store the new prices")
    new_list = half_prices(list)
    print(list)
    print(new_list)

    # shorter way to do the same thing
    print("One line of code to do the same(list comprehension)")
    half_price_list = [ item * .5 for item in list]
    print(half_price_list)

main()