import HW03_Yash_Gilda_dictionary as dic
import HW03_Yash_Gilda_wordle as wrd
# Begin
print("Welcome to Wordle")
gamesPlayed = 0
gamesWon = 0
guessDistribution = [0,0,0,0,0,0]
while(True):
    gamesPlayed += 1
    counter = 0
    wordle = dic.wordleAns()
    print(wordle)
    #print(dic.list)
    attempt_list = []
    while counter < 6:
        boolean = False
        user_input = input("Enter the word: ")
        user_input = user_input.lower()
        # Condition to check length of user input
        if len(user_input) == 0:
            quit()
        if len(user_input) != 5:
            print("The word must consist of 5 alphabets only")
            counter = counter - 1
        # Condition to check whether the user input contains only alphabets or not
        elif user_input.isalpha() == boolean:
            print("The word must consist of alphabets only")
            counter = counter - 1
        else:
            # Condition to check if user input is in the dictionary provided
            if user_input not in dic.list:
                print("Word is not in the Dictionary")
                counter = counter - 1
                attempt = 5 - counter
                print("Remaining Attempts: ", attempt)
            elif user_input in dic.list:
                if user_input not in attempt_list:
                    attempt_list.append(user_input)
                    # Condition to check if user input matches the wordle
                    if user_input == wordle:
                        gamesWon += 1
                        guessDistribution[counter] += 1
                        print("Congratulations! You have solved the Wordle!")
                        break
                    # Condition to call the compare_wordle function
                    else:
                        wrd.compare_wordle(user_input, wordle)
                        attempt = 5 - counter
                        print("Remaining Attempts: ", attempt)
                else:
                    # Condition to reset counter if the word is used previously
                    print("You have attempted this word earlier. Please try another word.")
                    counter = counter - 1
                    attempt = 5 - counter
                    print("Remaining Attempts: ", attempt)
        counter += 1
    if counter > 5:
        print("Sorry, but you have failed to solve the wordle!!! Please try again!!! ")
    print("GAME STATISTICS")
    print(f"Number of games played {gamesPlayed}")
    print(f"Win percentage {(gamesWon*100/gamesPlayed): .2f}")
    print(f"Guessed in 1st attempt: {guessDistribution[0]}")
    print(f"Guessed in 2nd attempt: {guessDistribution[1]}")
    print(f"Guessed in 3rd attempt: {guessDistribution[2]}")
    print(f"Guessed in 4th attempt: {guessDistribution[3]}")
    print(f"Guessed in 5th attempt: {guessDistribution[4]}")
    print(f"Guessed in 6th attempt: {guessDistribution[5]}")




