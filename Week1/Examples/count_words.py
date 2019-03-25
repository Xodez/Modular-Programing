poem = open("text.txt")

for line in poem:
    line = line.rstrip()
    words = line.split()
    number_of_words = len(words)
    print('"' + line + '" -- ' + str(number_of_words) + " words" )

poem.close()