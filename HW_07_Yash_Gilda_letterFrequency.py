import csv
import string
wrd_occurence = dict( (key, [0,0,0,0,0]) for key in string.ascii_lowercase )
myList = []
#Calculates the Letter Likelihood
def letter_likelihood():
    r = open("word_list.txt", "r")
    files = r.read()
    dictList = files.split("\n")
    myList = list(dictList)
    r.close()
    for wrd in myList:
        count = 0
        for letter in wrd:
            wrd_occurence[letter][count] += 1
            count+=1
    
    for letter in string.ascii_lowercase:
        flag = 0
        for wrd in myList:
            flag += 1
        for i in range(5):
            wrd_occurence[letter][i] = round((wrd_occurence[letter][i] / flag),4)

    f = open("letterFrequency.csv", 'w')
    for letter in string.ascii_lowercase:
        f.write(f"{letter}, {wrd_occurence[letter][0]}, {wrd_occurence[letter][1]}, {wrd_occurence[letter][2]}, {wrd_occurence[letter][3]}, {wrd_occurence[letter][4]}\n")

    return wrd_occurence

#Converting the list to Tuple
def list_To_tuple(diction):
    for key in diction.keys():
        diction[key] = tuple(diction[key])
    return diction

#Convert the Statistics into a Dictionary of Tuples
def statsTodicTuples():
    file = open("letterFrequency.csv")
    csvreader = csv.reader(file)
    wrd_occurence_csv = {}
    for row in csvreader:
        wrd_occurence_csv[row[0]] = (row[1], row[2], row[3], row[4], row[5])
    #print(word_occurence_csv)
    file.close()
    return wrd_occurence_csv

#Calculates the Occurence Likelihood      
def occ_likelihood():
    occ_like = {}
    if check_len(wrd):
        for wrd in myList:
            occurence_likelihood = float(wrd_occurence[wrd[0]][0]) * float(wrd_occurence[wrd[1]][1]) * float(wrd_occurence[wrd[2]][2]) * float(wrd_occurence[wrd[3]][3]) * float(wrd_occurence[wrd[4]][4])
            if check_likelihood_range(occurence_likelihood):
                occ_like[wrd] = occurence_likelihood

    sorted_list = sorted(occ_like.items(), key=lambda x:x[1])
    sorted_list.reverse()
    f = open("wordRank.csv", 'w')
    f.write("Rank, Word, Likelihood \n")
    flag = 1
    for wrd in sorted_list:
        f.write(f"{flag}, {wrd[0]}, {wrd[1]}\n")
        flag += 1
    f.close()
    return sorted_list

#Checks the length of the word
def check_len(wrd):
    if len(wrd) == 5:
        return True
    else:
        return False

def check_likelihood_range(likelihood):
    if likelihood<1:
        return True
    else:
        return False


#print(letter_likelihood())
#print()
#print(list_To_tuple(wrd_occurence))
#print()
#print(statsTodicTuples())
#print()
#print(occ_likelihood())