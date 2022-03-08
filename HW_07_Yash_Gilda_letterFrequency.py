import csv
import string
import HW03_Yash_Gilda_dictionary as dic
wrd_occurence = dict( (key, [0,0,0,0,0]) for key in string.ascii_lowercase )
def letter_likelihood():
    #wrd_occurence = dict( (key, [0,0,0,0,0]) for key in string.ascii_lowercase )
    for wrd in dic.myList:
        count = 0
        for letter in wrd:
            wrd_occurence[letter][count] += 1
            count+=1
    
    for letter in string.ascii_lowercase:
        flag = 0
        for wrd in dic.myList:
            flag += 1
        for i in range(5):
            wrd_occurence[letter][i] = round((wrd_occurence[letter][i] / flag),4)

    f = open("letterFrequency.csv", 'w')
    for letter in string.ascii_lowercase:
        f.write(f"{letter}, {wrd_occurence[letter][0]}, {wrd_occurence[letter][1]}, {wrd_occurence[letter][2]}, {wrd_occurence[letter][3]}, {wrd_occurence[letter][4]}\n")

    return wrd_occurence

def list_To_tuple(diction):
    for key in diction.keys():
        diction[key] = tuple(diction[key])
    return diction

def statsTodicTuples():
    file = open("letterFrequency.csv")
    csvreader = csv.reader(file)
    wrd_occurence_csv = {}
    for row in csvreader:
        wrd_occurence_csv[row[0]] = (row[1], row[2], row[3], row[4], row[5])
    #print(word_occurence_csv)
    file.close()
    return wrd_occurence_csv
        
def occ_likelihood():
    occ_like = {}
    for wrd in dic.myList:
        occurence_likelihood = float(wrd_occurence[wrd[0]][0]) * float(wrd_occurence[wrd[1]][1]) * float(wrd_occurence[wrd[2]][2]) * float(wrd_occurence[wrd[3]][3]) * float(wrd_occurence[wrd[4]][4])
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


print(letter_likelihood())
print()
print(list_To_tuple(wrd_occurence))
print()
print(statsTodicTuples())
print()
print(occ_likelihood())