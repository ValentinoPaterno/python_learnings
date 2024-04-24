# def addition(num1,num2):
#     result = num1 + num2
#     return result
# print(addition(1,2))

# # Syntax of a function with Parameters
# def function_name(parameter):
#     return parameter*2
# argument = 1
# print(function_name(argument)) # When we declare the function we call it parameter but when we call it we say that it's an argument

# # Function with 2 Parameters
# def sum_two_numbers (num_one, num_two):
#     sum = num_one + num_two
#     return sum
# print('Sum of two numbers: ', sum_two_numbers(1, 9))

# # Passing arguments with key and value
# def add_two_numbers (num1, num2):
#     total = num1 + num2
#     return total
# print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter

# # Function with default parameters -> If we don't pass arguments when calling the function, their default value will be used.
# def greetings (name = 'NN'):
#     message = name + ', welcome to Python for Everyone!'
#     return message
# print(greetings())
# print(greetings('Asabeneh'))

# # Arbitrary Number of Arguments
# # By adding the '*' before the parameter name, the function will take an arbitrary number of arguments
# def sum_all_nums(*nums):
#     total = 0
#     print(*nums)
#     for num in nums:
#         total += num
#     return total

# # Default and arbitrary number of Parameters
# def generate_groups (team,*args):
#     print(team)
#     for i in args:
#         print(i)
# print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

# #You can pass functions around as parameters
# def square_number (n):
#     return n * n
# def do_something(f, x):
#     return f(x)
# print(do_something(square_number, 3)) # 27

# --------------------------------- Ejercicios ---------------------------------
# # 1
# def add_two_numbers(n1,n2):
#     return n1+n2
# print(add_two_numbers(5,10))
# # 2
# def area_of_circle(radio):
#     result = 3.14 * (radio ** 2)
#     print(f"The area of a circle with radius: {radio} is: ")
#     return result
# print(area_of_circle(10))
# # 3
# def add_all_nums(*params):
#     result = 0
#     for i in params:
#         result += i 
#     return result
# print(add_all_nums(1,5,4))
# # 4 
# def convert_celcius_to_fahrenheit(grades):
#     conversion = (grades * (9/5)) + 32
#     return conversion
# print(convert_celcius_to_fahrenheit(10))
# # 5
# def check_season(month):
#     season = ""
#     month = month.lower()
#     if month in ("december", "january", "february"):
#         season = "Winter"
#     elif month in ("march", "april", "may"):
#         season = "Spring"
#     elif month in ("june", "july", "august"):
#         season = "Summer"
#     elif month in ("september", "october", "november"):
#         season = "Autum"
#     else: 
#         season = "Error. Not a valid month"
#     return season
    
# print(check_season("DECEMBER"))
# # 6
# def calculate_slope(x2,x1,y2,y1):
#     slope = (y2 - y1)/(x2 - x1)
#     return slope
# # 7
# # 8
# def print_list(list): 
#     for element in list:
#         print(element)

# lst = ["pepe", "pipo", "popo"]
# print_list(lst)
# # 9 
# def reverse_list(list):
#     i = len(list) - 1 
#     reversed_lst = []
#     while i >= 0:
#         reversed_lst.append(list[i])
#         i -= 1
#     return reversed_lst

# lst = [0,1,2,3,4,5,6,7,8,9,10]
# print(reverse_list(lst))
# # 10
# def capitalize_list_items(list):
#     new_list = []
#     for element in list:
#         new_list.append(element.upper())
#     return new_list

# lst = ["argentina","bolivia","brasil"]
# print(capitalize_list_items(lst))
# # 11
# def add_item(list, item):
#     list.append(item)
#     return list
# lst = ["banana","pepe","popo"]
# add_item(lst, 1)
# print(lst)
# # 12
# def remove_item(list_name, item):
#     return list_name.remove(item)
# lst = [1,2,3,4]
# remove_item(lst, 2)
# print(lst)
# # 13 
# def sum_of_number(number):
#     result = 0
#     for i in range (0, number+1):
#         result += i 
#     return result
# print(sum_of_number(5))

# # LEVEL 2 
# # 1
# def evens_and_odds(number):
#     odds = 0
#     evens = 0
#     if number < 0:
#         return "Error, debe ser un numero positivo"
#     else:
#         for i in range(0,number+1):
#             if(i % 2) == 0:
#                 evens +=1 
#             else:
#                 odds += 1
#         return evens, odds 
    
# print(f"The number of odds are: {evens_and_odds(100)[1]}\nThe number of evens are: {evens_and_odds(100)[0]}")
# 2
# def is_empty(param):
#     if not param:
#         return True
#     else:
#         return False
# arg = "hola"
# print(is_empty(arg))