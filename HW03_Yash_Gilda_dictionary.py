import random
#Function to remove blank spaces from the dictionary
def remove(string):
    return string.replace("\n", "")
myList = []
#Imports the dictionary
d = open("words.txt", "r")
f = open("word_list.txt", "w")
for x in d:
    x = remove(x)
    if len(x) == 5:
        myList.append(x)
        f.write(x+"\n")
f.close()
#Chooses the wordle
def wordleAns():
    #return random.choice(list)
    r = open("word_list.txt", "r")
    files = r.read()
    dictList = files.split("\n")
    finalList = list(dictList)
    wordle = random.choice(finalList)
    r.close()
    return wordle

