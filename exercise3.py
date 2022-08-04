#Exercise 3, comparisons and iterations with lists
#Imports

#Initalising variables
#List of numbers we're going to be working on
number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lesser_than_five = []
user_lesser_than = 0
#User input limit for extra task
user_lesser_than_list = []
#User input
user_lesser_than = int(input("Enter the number that you want all other numbers in the new list to be lower than: "))

#List iteration via for
for number in number_list:
    #We have a term of the list as number, now we compare with limit and append to the new list
    if number < 5:
        lesser_than_five.append(number)
    #Identical process for user generated number
    if number < user_lesser_than:
        user_lesser_than_list.append(number)

#Printing lesser_than_five list directly and through iteration
print(lesser_than_five)
for lesser_than_five_iterator in lesser_than_five:
    print(lesser_than_five_iterator)

#Same process for the user limit based list
print(user_lesser_than_list)
for user_lesser_than_list_iterator in user_lesser_than_list:
    print(user_lesser_than_list_iterator)