def main():
    nameslist1 = [ "Ted", "Fred", "Tom"]
    nameslist2 = [ "Ed", "Len", "Bob"]
    # print first name is list1
    # print last name in list2
    print(nameslist1[0])
    print(nameslist2[-1])

    all_names = nameslist1 + nameslist2
    print(all_names)
    # print names at [0], [2], [4]
    print(all_names[0:5:2])

    if "Ed" in all_names:
        print("found Ed")

    # print first letter ([0]) of last name
    print(all_names[-1][0])

    # concatenate (add) first names of list1 and list2
    names = nameslist1[0] + nameslist2[0]
    print(names)
    # printing all names in list1
    print("List 1: ")
    for i in nameslist1:
        print(i)
    print()
    # print each character in names
    for i in names:
        print(i)
    print()
    print(len(nameslist1)) # print length of nameslist1
    # print the index and the value of items in nameslist1
    for x,n in enumerate(nameslist1):
        print(x, n)


main()