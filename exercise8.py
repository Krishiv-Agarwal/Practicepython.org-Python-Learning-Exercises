#Exercise 8, Rock Paper and Scissors game
#INIT variables and imports

user1_name = str()
user1_choice = str()
user1_score = int()
user1_won = bool()

user2_name = str()
user2_choice = str()
user2_score = int()
user2_won = bool()

quit_game = str()
draw = bool()

#Just to put a new message if someone plays a second round so it doesnt feel like they just repeating the same block of code again and again which is basically what is happening though
firsttime = True

#Main while loop to keep program running until user asks to quit

#Corny introduction messages to make it a bit more fun
print("\nWelcome to Paper Co, where we provide an offline service to play rock paper and scissors with a friend.")
print("========================================================================================================")

#User info input to make it more personalised
user1_name = str(input("Hello, what would the first user like to call themselves: "))
user2_name = str(input("Hello, what would the second user like to call themselves: "))

print("""\nThe game will now begin.
You have 3 options to choose from. Entering the incorrect string will prompt a re-enter.
Rock
Paper
Scissors
=====================================================================================\n""")

#While loop for the game itself
while True:
    if firsttime == False:
        print("Welcome back! Another round eh?")
    #Entering inital input
    user1_choice = str(input("Hey " + str(user1_name) + ", what would you like to choose? Rock, Paper or Scissors? "))
    #Checking if input is correct and asking for re-entry if not
    while True:
        if user1_choice == "Rock" or user1_choice == "Paper" or user1_choice == "Scissors":
            break
        else:
            user1_choice = str(input("Hey " + str(user1_name) + ", you entered the incorrect input. Please re-enter, remember the keywords are Rock, Paper or Scissors: "))

    #Same thing here
    user2_choice = str(input("Hey " + str(user2_name) + ", what would you like to choose? Rock, Paper or Scissors? "))

    while True:
        if user2_choice == "Rock" or user2_choice == "Paper" or user2_choice == "Scissors":
            break
        else:
            user2_choice = str(input("Hey " + str(user2_name) + ", you entered the incorrect input. Please re-enter, remember the keywords are Rock, Paper or Scissors: "))
    #Now doing the comparisons
    #First we do comparisons for all win conditionos of user1
    if user1_choice == "Paper" and user2_choice == "Rock":
        user1_won = True
    elif user1_choice == "Scissors" and user2_choice == "Paper":
        user1_won = True
    elif user1_choice == "Rock" and user2_choice == "Scissors":
        user1_won = True
    #Now we do all draw conditions
    elif user1_choice == "Rock" and user2_choice == "Rock":
        draw = True
    elif user1_choice == "Paper" and user2_choice == "Paper":
        draw = True
    elif user1_choice == "Scissors" and user2_choice == "Scissors":
        draw = True
    #For all win conditions of user 2 we could use an else statement
    #but its kind of bad practice because we might still fuck up in verification and i dont want the program failing
    #ill just copy paste the first block of code and change the names lol
    elif user2_choice == "Paper" and user1_choice == "Rock":
        user2_won = True
    elif user2_choice == "Scissors" and user1_choice == "Paper":
        user2_won = True
    elif user2_choice == "Rock" and user1_choice == "Scissors":
        user2_won = True
    #If there is an error even though i made so many checks and balances ill just restart the program
    else:
        print("Input error; Restarting program")
        break

    print("\n")
    #The reason why i bothered with setting up variables with this stuff instead of outputting the message there itself is because here i can make much more complex outputs with significantly less amount of repeated code
    if user1_won == True:
        print("Congratulations " + str(user1_name) + ", you have won! Your score is now " + str(user1_score))
        user1_score += 1
    elif user2_won == True:
        print("Congratulations " + str(user2_name) + ", you have won! Your score is now " + str(user2_score))
        user2_score += 1
    else:
        print("Scoring error; restarting program")
        break

    #Now to check if they want to quit

    print("\nHope you had fun playing this round of Rock, Paper and Scissors. ")
    print("To reiterate " + str(user1_name) + " has a score of " + str(user1_score) + " and " + str(user2_name) + " has a score of " + str(user2_score) + ".")

    quit_game = str(input("\nDo you want to quit the game. If you do not want to quit, enter any phrase OTHER than quit. If you do want to quit, enter the phrase 'Quit': "))
    if quit_game == "Quit":
        print("\n Thank you for playing at Paper Co.")
        break
    else:
        firsttime = False
        continue


