
word_count= {}

with open("/Users/richardwittich/VS Code/poem.txt", "r") as file:
    for x in file:
       words = x.split(" ")
       for y in words:
          if y in word_count:
             word_count[y]+=1
          else:
             word_count[y]=1

print(word_count)

word_occurances = list(word_count.values())
print("Max occurances of any word is:",word_occurances)
max_count = max(word_occurances)
print("Max occurances of any word is:",max_count)

print("Words with max occurances are: ")
for word, count in word_count.items():
    if count==max_count:
        print(word)