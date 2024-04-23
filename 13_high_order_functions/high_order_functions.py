"""
In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

1) A function can take one or more functions as parameters
2) function can be returned as a result of another function
3) function can be modified
4) function can be assigned to a variable
In this section, we will cover:

- Handling functions as parameters
- Returning functions as return value from another functions
- Using Python closures and decorators
"""
# # Function as a Parameter
# def sum_numbers(nums):
#     return sum(nums) # a sad function abusing the built-in sum function :<

# def high_ord_function(f, lst): # function as a parameter
#     summation = f(lst)
#     return summation

# print(high_ord_function(sum_numbers, [1,2,3,4,5]))

# # Function as a Return Value
# def square(x):
#     return x ** 2

# def cube(x):
#     return x ** 3

# def absolute(x):
#     if x >= 0:
#         return x 
#     else: 
#         return -(x)

# def high_order_function(type): # a high order function returning a function
#     if type == "square":
#         return square
#     elif type == "cube":
#         return cube 
#     elif type == "absolute":
#         return absolute

# result = high_order_function('square')
# print(result(9))
# result = high_order_function('cube')
# print(result(2))
# result = high_order_function('absolute')
# print(result(-2))

