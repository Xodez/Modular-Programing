#  Name: show_names
#  Desc:   pass a list to a method and print the contents
#          illustrates three ways to iterate over a list
def print_list(names):
    for item in names:
        print(item)
    print()
    for i in range(len(names)):
        print(str(i) + ".  "+ names[i])
    print()
    for i, item in enumerate(names):
        print(str(i) + ".  " + item)

def main():
    counties = ["Kerry","Cork","Waterford", "Limerick", "Tipp"]
    print_list(counties)

main()