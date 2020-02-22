# 3a.
import random
wordList = ["champion", "meticulous", "hexagon"]
random.shuffle(wordList)
getWord = list(wordList[0])
random.shuffle(getWord)
getWord = " ".join(getWord)
print(getWord)


