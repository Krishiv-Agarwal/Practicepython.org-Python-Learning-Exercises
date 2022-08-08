#Exercise 14, sets
#INIT
#Imports
import random

#Functions
#Creates a random list based on list length
def list_constructor(list_length):
    constructed_list = []
    #Using randrange rather than sample because that's what the question required
    for iterator in range(1, list_length):
        constructed_list.append(random.randrange(1, 10))
    
    return constructed_list

#Removes duplicates from a list
def no_more_doubles(number_list):
    #Sets cannot have duplicates and can be easily converted to and from list
    number_list = set(number_list)
    number_list = list(number_list)
    return number_list

#Variables

list_length = int()
list_with_duplicates = list()
list_no_duplicates = list()

#User input
list_length = int(input("\nPlease enter the maximum length of the list that you want generated: "))

#Generating list
list_with_duplicates = list_constructor(list_length)

print("This is the list that was generated " + str(list_with_duplicates))

#Removing common terms
list_no_duplicates = no_more_doubles(list_with_duplicates)

print("This is the list without any duplicates " + str(list_no_duplicates))