#  Name: update_prices1
#  Desc:   modify a list in a method
def  half_prices(list):
    for i in range(len(list)):
        list[i] = list[i]/2

def main():
    list = [ 40.00, 30.50, 1.10, 99.00]
    print("Initial Price list")
    print(list)
    print("Updated Price list")
    half_prices(list)
    print(list)

main()
