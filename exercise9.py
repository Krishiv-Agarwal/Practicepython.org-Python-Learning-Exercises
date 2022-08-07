#Exercise 9, Guessing Game
#INIT

#To randomly generate the number
import random

#INIT variables
answer = int()
guess = int()
username = str()

#Generating answer
answer = random.randrange(1,9,1)

#Introductory message
print("\n Welcome to Venn Industries, we will be providing you with the experience of playing against the odds themselves. A guessing game.")
print("============================================= Program INIT =========================================================================")

#User input name
username = str(input("\nBefore we start the game, it'd be great to know your name: "))

#Creating loop for guesses
while True:
    #Inputting guess
    guess = int(input("\nOkay " + str(username) + ", please enter your guess in between 1 to 9: "))
    #Checking if guess is in range
    while True:
        if guess in [1,2,3,4,5,6,7,8,9]:
            break
        else:
            guess = int(input("That was an incorrect input " + str(username) + ", please re-enter your guess in between 1 to 9: "))

    #Basic comparisons with output for each
    if int(guess) == int(answer):
        print(str(username) + ", you guessed correctly! The answer was " + str(answer) + ".")
        break
    elif int(guess) < int(answer):
        print(str(username) + ", you've guessed too low! Your guess was " + str(guess) + ".")
    elif int(guess) > int(answer):
        print(str(username) + ", you've guessed too high! Your guess was " + str(guess) + ".")

print("\nVenn Industries thanks you for choosing us!")
