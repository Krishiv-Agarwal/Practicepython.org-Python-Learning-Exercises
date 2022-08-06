#Exercise 6, finding strings that are identical forward and backwards
#INIT vars and imports

user_string = ""
palindrome = False

#Inputting the string

print("A palindrome is a string that is identical forwards and backwards")
user_string = str(input("Enter a string you think is a palindrome: "))

#Checking if the string is a palindrome

if user_string == user_string[::-1]:
    palindrome = True

#Output

if palindrome == True:
    print("The string '" + str(user_string) + "' is a palindrome.")
else:
    print("The string '" + str(user_string) + "' is not a palindrome.")