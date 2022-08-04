#Exercise 2, finding even or odd
#Initalising variables

user_number = 0
#Check is a part of the extras in the exercise, essentially I just need to check if the check is a factor of the number.
user_check = 0
oddoreven = False
multipleoffour = False
multipleofcheck = False
#Inputting user data
user_number = int(input("Please enter a number to check if it is odd or even: "))
user_check =  int(input("Please enter a number to check if it is a factor of the previously entered number: "))

#Finding whether user_number is odd or even and also other conditionals
if user_number % 2 == 0:
    oddoreven = True
#Checking to see if the number is divisble by four
if user_number % 4 == 0:
    multipleoffour = True
if user_number % user_check == 0:
    multipleofcheck = True

#Printing
if oddoreven == True:
    print("User number, " + str(user_number) +  " is Even.")
elif oddoreven == False:
    print("User number, " + str(user_number) + " is Odd.")
if multipleoffour == True:
    print("User number, "  + str(user_number) + " is a multiple of 4. ")
if multipleofcheck == True:
    print("User number, "  + str(user_number) + " is a multiple of "  + str(user_check) + ".")
