""" 
Python uses try and except to handle errors gracefully. A graceful exit (or graceful handling) 
of errors is a simple programming idiom -a program detects a serious error condition and "exits 
gracefully", in a controlled manner as a result. Often the program prints a descriptive error 
message to a terminal or log as part of the graceful exit, this makes our application more robust. 
The cause of an exception is often external to the program itself. An example of exceptions could 
be an incorrect input, wrong file name, unable to find a file, a malfunctioning IO device. 
Graceful handling of errors prevents our applications from crashing.
"""
# Syntax Example
""" 
try:
    run this code
except: -> (May or may not have a condition)
    execute this code when there is an exception
else:
    No exceptions? -> Run this code
finally: 
    Always run this code
"""


# try:
#     print(10+"5")
# except:
#     print("Something went wrong")

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type Error ocurred')

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occur')
# except ValueError:
#     print('Value error occur')
# except ZeroDivisionError:
#     print('zero division error occur')
# else:
#     print('I usually run with the try block')
# finally:
#     print('I alway run.')

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except Exception as e:
#     print(e)

# ----------- Packing and Unpacking Arguments in Python ----------- 
# We use * for tuples, ** for dictionaries

# def sum_of_five_nums(a,b,c,d,e):
#     return a + b + c + d + e 

# lst = [1,2,3,4,5]
# print(sum_of_five_nums(*lst)) 

# numbers = range(2, 7)  # normal call with separate arguments
# print(list(numbers)) # [2, 3, 4, 5, 6]
# args = [2, 7]
# numbers = range(*args)  # call with arguments unpacked from a list
# print(numbers)      # [2, 3, 4, 5,6]

# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
# numbers = [1, 2, 3, 4, 5, 6, 7]
# one, *middle, last = numbers
# print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

# def unpacking_person_info(name, country, city, age):
#     return f'{name} lives in {country}, {city}. He is {age} year old.'

# dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
# print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.