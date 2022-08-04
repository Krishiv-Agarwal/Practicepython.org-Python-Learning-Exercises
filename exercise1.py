#Exercise 1, finding years till hundred
#Importing to datetime module to find the correct year
from datetime import date

#Initialising variables
user_age = 0
user_result_repetition = 0
year = date.today()
year_till_hundred = year.year

#Testing datetime
print(year.year)

#Inputting user data
user_age = int(input("Please enter your age: "))
user_result_repetition = int(input("Please input how many times do you the final message to be repeated: "))

#Calculating year till hundred
year_till_hundred += (100 - user_age)

#Printing results and string concantation for repeating final message
print(("You will be 100 years old in the year " + str(year_till_hundred) + "." + "\n") * user_result_repetition)