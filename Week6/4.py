def getWantedLenght(wordList, lenght):
    wantedWords = ""
    print(wordList)
    splitter = int(lenght)
    for i in range(len(wordList)):
        if len(wordList[i]) == int(splitter):
            wantedWords = str(wantedWords) + " " + str(wordList[i])
    return wantedWords


def main():
    sentence = "i know some new tricks, said the cat in the hat. a lot of good tricks."
    desiredLenght = sentence.split(" ")
    jeff = getWantedLenght(desiredLenght, 3)
    print(jeff)


main()
