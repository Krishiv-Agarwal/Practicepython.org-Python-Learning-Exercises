#Exercise 11, determine if prime
#INIT

def first_and_last_finder(list):
    #Will return the first (1) and the last (-1) terms on the list
    return  [list[0], list[-1]]

#Variables
user_list = list()
first_and_last_term = list()
iterator = int()

#Inputting user list
for iterator in range(1,6,1):
    #Adding user numbers to user list
    user_list.append(int(input("Enter the next number you want on the list: ")))
print(user_list)

#Generating list with first and last terms
#appending the returned quantity
first_and_last_term.append(first_and_last_finder(user_list))
 
 #Output
for iterator in first_and_last_term:
    print(iterator)