# USE main()!!!!! IT AVOIDS MISUNDERSTANDING IN CODE

# x and y are local variables - parameters - created
# when the function is called.
# product is a local variable created in the first line
# of the function
# All local variables are destroyed when the function finishes.
def multiply(x, y):
    product = x * y
    return product


def print_product(w, z, p):
    print("{} x {} = {}".format(w, z, p))


def main():
    a = 4
    b = "Hello"
    # a is an integer so x becomes an integer with value 4
    # b is a String so x becomes a String with value "Hello"
    result = multiply(a, b)  # stores the returned value in result
    # print() is a void function so
    print_product(a, b, result)

    a = 5.3
    b = 7
    # a is a float so x becomes a float whose value is 5.3
    # b is an integer so y becomes an integer whose value is 7
    result = multiply(a, b)  # stores the returned value in result
    print_product(a, b, result)

    print(print_product(a,b,result))


main()
