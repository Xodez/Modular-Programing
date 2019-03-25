print("The data from the file")
print("----------------------")

data_file = open("numbers.txt")

total = 0.0

for line in data_file:
    next_number = line.rstrip()
    print(next_number)
    total += float(next_number)

print("\n\nTotal >>> {:.1f}".format(total))

data_file.close()