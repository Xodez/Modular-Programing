def target_times(time_taken,names):

    for i in range(len(time_taken)):
        timeOld = time_taken[i]
        timeNew = ((timeOld/100)*90)
        nameUser = names[i]
        # print ("{0:.2f}".format(timeNew),nameUser)
        return timeNew,nameUser

def main():

    time_taken = [32, 27, 23, 26, 26, 18]
    names = ["Ann", "Joe", "Pat", "Ken", "Ali", "Ger"]
    # newStuff = target_times(time_taken, names)
    print(target_times(time_taken, names))

main()
