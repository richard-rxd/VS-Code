import os

wordcount = {}

with open(os.path.join(os.path.dirname(__file__), "poem.txt") , "r") as poem:
    for line in poem:
        words = line.split(" ")
        for word in words:
            word = word.replace("\n", "")
            if word in wordcount:
                wordcount[word] += 1
            else:
                wordcount[word] = 1

print(wordcount)