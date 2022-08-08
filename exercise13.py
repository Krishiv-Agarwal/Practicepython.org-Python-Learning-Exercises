#Exercise 13, Fibbonaci Generator
#INIT

#Functions
def fibbonaci_generator(limit):
    #The variable where we store the multiplied numbers
    value_storage = 1
    #Regular iteration
    for iterator in range(1, limit + 1, 1):
        print("The next fibbonaci value is " + str(value_storage) + " and the next number multiplying is " + str(iterator) + ".")
        value_storage *= limit
    #Returning fibbonaci value
    return value_storage

#Variables
user_limit = int()
fibbonaci = int()

#Inputs
user_limit = int(input("\nPlease enter the number you want to generate a fibbonaci sequence till: "))

#Generating the sequence
fibbonaci = fibbonaci_generator(user_limit)

print(fibbonaci)
