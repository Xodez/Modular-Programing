#  Name: calculate_total
#  Desc:  methods to calculate total and average
def get_total( numbers_list):
    total = 0
    for i in numbers_list:
        total = total + i
    return total

def get_average(numbers_list ):
    total = get_total(numbers_list)
    amount = len(numbers_list)
    average = 0;
    if (amount != 0 ):
        average = total/amount
    return average

def main():
    ages  = [ 10, 22, 13, 14, 19]
    distances = [ 500]
    total = get_total(ages)
    avg = get_average(ages)
    print("The total is " +str(total))
    print("The average is " +str(avg))
main()
