#Exercise 15, string manipulation II
#INIT

#Functions
#Reverses string
def string_reverse(word):
    #First we split the string into list of individual words
    result = word.split()
    #Re-order the words
    result = result[::-1]
    #Join em back
    result = " ".join(result)
    return result

#Variables
user_string = str()
reversed_string = str()

#Input
user_string = str(input("\nPlease enter the string that you want reversed: "))

#Reversing string
reversed_string = string_reverse(user_string)

#Output
print("The reversed version of '" + str(user_string) + "' is '" + str(reversed_string) + ".'")
