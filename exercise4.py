#Exercise 4, finding divisors of inputted number
#INIT variables

user_number = 0
divisor_list = []
divisor_iterator = 0

#Inputs

user_number = int(input("Enter the number you want to find the divisors of: "))

#Iteration

#Iterating through all potential divisors
for divisor_iterator in range(1, user_number + 1):
    if user_number % divisor_iterator == 0:
        divisor_list.append(divisor_iterator)
#Output

#Iterating through divisor_list to print all Iterators
print("This is the list of divisors for the number " + str(user_number), end=": ")
for divisor_iterator in divisor_list:
    print(str(divisor_iterator), end=", ")