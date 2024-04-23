"""
List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. 
List comprehension is considerably faster than processing a list using the for loop.
-- Syntax:
[i for i in iterable if expression]
"""
# List comprehension
# language = 'python'
# lst = [i for i in language]
# print(type(lst), lst)
# # Generating Numbers
# numbers = [i for i in range(11)]
# print(numbers)
# # Using Mathematical Operations
# squares = [i * i for i in range(11)]
# print(squares)
# # Making a list of tuples
# numbers = [(i*i, i) for i in range(11)]
# print(numbers)

# Using 'if' expression
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)
# Filter numbers
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)
# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
