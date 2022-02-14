#Wordle
#Pseudocode
#This program is an attempt to implement the Wordle game

#function compare_wordle(Argument one, Argument two){

    #FOR every character in the two strings compare with each other
        #IF a character is equal to a character in the wordle THEN it checks
            #if the letter is in the same position as the wordle
                #print prompt "(The character) is in the correct position"
            #ELSE
                #print prompt "(The character) is in the wordle but not in the correct position"
            #ENDIF
        #ENDIF
#end
#}

#{
#In the main function
    #print prompt "Welcome to Wordle"
    #Initialize the counter to 0, declare the wordle "SONAR", initialize the user attempt_list

    #WHILE counter < 6
    #{
        #Initialize boolean to False
        #print prompt "Enter the word: "
        #Accept user_input from the user and convert it to Upper Case
        #IF the user_input length is not equal to 5 THEN
            #print prompt "The word must consist of 5 alphabets only"
            # counter is reduced by 1
        #ELSE IF the user_input contains anything but alphabets
            #print prompt "The word must consist of alphabets only"
        #ELSE
            #IF the user_input is not in the attempt_list THEN add the user_input to the attemp_list
                #IF the user_input is equal to the wordle THEN
                    #print prompt "Congratulations! You have solved the Wordle!"
                    #BREAK
                #ELSE call the function compare_wordle(user_input, wordle)
                    #Initialize an attempt counter equal to 5-counter
                    #print prompt "Remaining Attempts: " (attempt)"
            #ELSE
                #print prompt "You have attempted this word earlier. Please try another word."
                #Decrement the counter by 1 and #Initialize an attempt counter equal to 5-counter
                #print prompt "Remaining Attempts: " (attempt)"
    #Increment counter by 1
    #}ENDWHILE
#IF counter is greater than 5 THEN
    #print prompt"Sorry, but you have failed to solve the wordle!!! Please try again!!! "

#Code
#Function to compare the Wordle
def compare_wordle(str1, str2):
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    #Condition to check if the letter is in correct position
                    if i == j:
                        print(str1[i]+" is in the correct position")
                    else:
                        print(str1[i]+" is present in the wordle but not in the correct position")


#Begin
print("Welcome to Wordle")
counter = 0
wordle = "SONAR"
attempt_list = []

while counter < 6:
    boolean = False
    user_input = input("Enter the word: ")
    user_input = user_input.upper()
    #Condition to check length of user input
    if len(user_input) != 5:
        print("The word must consist of 5 alphabets only")
        counter = counter-1
    # Condition to check whether the user input contains only alphabets or not
    elif user_input.isalpha() == boolean:
        print("The word must consist of alphabets only")
        counter = counter-1
    else:
        # Condition to check if user input is repeated
        if user_input not in attempt_list:
            attempt_list.append(user_input)
            #Condition to check if user input matches the wordle
            if user_input == wordle:
                print("Congratulations! You have solved the Wordle!")
                break
            #Condition to call the compare_wordle function
            else:
                compare_wordle(user_input, wordle)
                attempt = 5-counter
                print("Remaining Attempts: ", attempt)
        else:
            #Condition to reset counter if the word is used previously
            print("You have attempted this word earlier. Please try another word.")
            counter = counter-1
            attempt = 5 - counter
            print("Remaining Attempts: ", attempt)
    counter += 1
if counter > 5:
    print("Sorry, but you have failed to solve the wordle!!! Please try again!!! ")

