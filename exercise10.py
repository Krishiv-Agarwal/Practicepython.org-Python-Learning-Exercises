#Exercise 10, list comprehensions (again)
#INIT

#Importing to generate two random lists
import random

list1 = list()
list2 = list()
common = list()
iterator = int()

#Generating both lists
list1 = random.sample(range(1,100,1), 50)
list2 = random.sample(range(1,100,1), 50)

#finding common terms
for iterator in list1:
    if iterator in list2:
        common.append(iterator)

#Sorting common terms in ascending
common.sort()

#Output
print(common)