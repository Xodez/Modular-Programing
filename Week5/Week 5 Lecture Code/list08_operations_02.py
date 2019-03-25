results = [80, 45, 67, 91, 49]
# pop removes an item from the list but returns it so it can be stored.
# based on the index
print("Before popping:", results)
# pop and return the last item
item1 = results.pop()
print("After popping pop():", results)
print("{} was popped".format(item1))

# pop and return the item at index 2
item2 = results.pop(2)
print("After popping pop(2):", results)
print("{} was popped".format(item2))

item3 = results.pop(-1)
print("After popping pop(-1):", results)
print("{} was popped".format(item3))

print("After popping:", results)

# count the number of occurrences of 80
print("There is/are", results.count(80), "instances of 80 in the list")

# remove and del achieve the same result
del(results[1])
print("After del on index 1:", results)

record = ["R001234567", "Donald", "Duck", 56]
print(record)
record.clear()
print(record)