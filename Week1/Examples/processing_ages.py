data_file = open("ages.txt")

while True:
    name = data_file.readline().rstrip()
    if name == "":
        break
    age = int( data_file.readline().rstrip() )
    print("{} is {} years old".format(name, age))

data_file.close()
