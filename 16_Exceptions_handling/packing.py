"""
Sometimes we never know how many arguments need to be passed to a python function. 
We can use the packing method to allow our function to take unlimited number 
or arbitrary number of arguments. 
"""

# # Packing Lists
# def sum_all(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
# print(sum_all(1, 2, 3))             # 6
# print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

# # Packing Dictionaries
# def packing_person_info(**kwargs):
#     # check the type of kwargs and it is a dict type
#     # print(type(kwargs))
#     # Printing dictionary items
#     for key in kwargs:
#         print(f"{key} = {kwargs[key]}")
#     return kwargs
# print(packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250))

# # Spreading in Python
# lst_one = [1,2,3]
# lst_two = [4,5,6]
# lst = [0, *lst_one, *lst_two]
# print(lst)


# Enumerate
# If we are interested in an index of a list, we use enumerate built-in
# function to get the index of each item in the list.
# country_lst_one = ['Finland', 'Sweden', 'Norway']
# country_lst_two = ['Denmark', 'Iceland']
# countries = [*country_lst_one, *country_lst_two]

# for index, i in enumerate(countries):
#     print(i, index)
#     if i == 'Finland':
#         print(f'The country {i} has been found at index {index}')
#         break