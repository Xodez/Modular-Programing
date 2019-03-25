print("Some String specefic methods")
lyrics = "Fly me to the moon"
pos = lyrics.find("me")
print("me" + " is at position/index" + str(pos))
new_lyrics = lyrics.replace("Fly", "Take")
print(lyrics)
print(new_lyrics)
print("convert the string to a list of words:")
list1 = lyrics.split()
print(list1)
print("Create a String from a list of words")
list2 = [ "this", "is", "a", "list"]
word = ''.join(list2)
print(word)