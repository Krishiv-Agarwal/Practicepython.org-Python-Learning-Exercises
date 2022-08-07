#Exercise 7, list comprehensions
#INIT variables and imports

user_numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_numbers = []
numbers_iterator = 0

#Filtering out user_number to find which ones are even and generating new list

for numbers_iterator in user_numbers:
    if numbers_iterator % 2 == 0:
        even_numbers.append(numbers_iterator)

#Output

print(even_numbers)