import random
#Function to remove blank spaces from the dictionary
def remove(string):
    return string.replace("\n", "")
list = []
#Imports the dictionary
d = open("/Users/yashgilda/desktopp/MSCS/Sem_2/SSW 810 /HW_03/words.txt", "r")
for x in d:
    x = remove(x)
    if len(x) == 5:
        list.append(x)
#Chooses the wordle
wordle = random.choice(list)

