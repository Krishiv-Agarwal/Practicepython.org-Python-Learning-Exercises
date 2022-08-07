#Exercise 11, determine if prime
#INIT

#Functions
def prime_number_calc(number):
    iterator = int()
    prime_number = False

    #Iterating through all positive integers until the numbers and dividing the number by them
    #2 as a starting number due to prime numbers being divisble by both 1 and itself.
    for iterator in range(2, number + 1, 1):
        if number % iterator != 0:
            prime_number = False
        else:
            prime_number = True
        return prime_number

#Variables
number = int()
prime_number = bool()

#Input
print("\nWelcome to prime number calculator!")
print("---------------INIT----------------")

number = int(input("Please enter the number that you want to check is prime: "))

#Checking if prime
prime_number = prime_number_calc(number)

if prime_number == True:
    print("\nThe number " + str(number) + " is a prime number.")
else:
    print("\nThe number " + str(number) + "is not a prime number.")