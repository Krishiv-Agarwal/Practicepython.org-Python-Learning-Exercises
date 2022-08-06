#Exercise 5, common terms between two random lists
#INIT vars and imports

import random

random_iterator = 0
list_1 = []
list_2 = []
common_terms = []

#Generating two random lists

#We use random iterator to cycle through a bunch of random numbers we generate via the randrange() function
for random_iterator in range(0, 21, 1):
    list_1.append(random.randrange(1, 100, 1))

#Repeat same process for list_2
for random_iterator in range(0, 21, 1):
    list_2.append(random.randrange(1, 100, 1))

#Outputting the lists

#Printing list 1
print("List 1: ", end=" ")
for random_iterator in list_1:
    print(str(random_iterator), end=", ")
print("\n")

#Print list 2
print("List 2:", end=" ")
for random_iterator in list_2:
    print(str(random_iterator), end=", ")
print("\n")

#Iterating to check if there are common terms
for random_iterator in list_1:
    if random_iterator in list_2:
        common_terms.append(random_iterator)

#Output

print("The common terms between the two lists")
for random_iterator in common_terms:
    print(str(random_iterator), end=", ")
