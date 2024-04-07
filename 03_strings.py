my_var = "Hola mundo"
print(len(my_var))

my_newLine_string = "Esto es un string\ncon salto de linea"
my_tab_string = "\tEsto es un string con tabulacion"

# Formateo de Strings 

# Old style Formatting (%s (strings), %d (int), %f (float))
    # Strings only
name, surname, city = "valentino", "paterno", "corrientes"
formated_string = "My name is %s %s and I live in %s" %(name, surname, city)
print(formated_string)
    # Str and Numbers
radius = 10
pi = 3.14 
area = (pi * radius) ** 2
formated_string = "The area of a circle with a radius %d is %.2f" %(radius,area)
print(formated_string)
    # Example with a list
py_libraries = ["Flask", "Django"]
formated_string = "These are 2 libraries from python: %s"%(py_libraries)
print(formated_string)

# New style Formatting (introduced in Python version 3)
    # Strings
name, surname, city = "valentino","paterno","corrientes"
formated_string = "My name is {} {} and I am from {}".format(name,surname,city)
print(formated_string)
    # Operations with numbers
a, b, c = 5, 4, 2
print("{} + {} = {}".format(a, b, a + b))
print("{} * {} = {}".format(a, b, a * b))
print("{}*{}/{} = {}".format(a,b,b, a*b/b))

# Strings Interpolation 
print(f"{a} + {b} = {a+b}")
print(f"{a} / {b} = {a/b:.3f}")

# Unpacking Characters in Strings
language = "Python"
a,b,c,d,e,f = language
print(a,b,c,d,e,f)

# Accessing characters in Strings by Index
print(language[0]) # Shows characters in 0 position (P)

# Slicing
sliced_language = language[1:3] # [1,3) 
print(sliced_language)
sliced_language = language[0:] # Picks every character after the 0 position included
print(sliced_language)
sliced_language = language[-1] # Goes from forward to backward
print(sliced_language)
sliced_language = language[::-1] # Reverses the direction of the word
print(sliced_language)
sliced_language = language[0:6:2] # Pto 
print(sliced_language)

# String Methods

challenge = "thirty days of python"
print(challenge.capitalize()) # Converts the 1st character of the string to capital letter
print(challenge.count("y")) # count(substring, start=, end=) start: start of counting, end= last index to count 
print(challenge.count("t",0,5))
print(challenge.endswith("on")) # checks if a string ends with a specified ending
challenge2 = 'thirty\tdays\tof\tpython'
print(challenge2.expandtabs()) # Replaces tab character with spaces, default tab size is 8. It takes tab size argument
print(challenge.find("r")) # Return the index of the first occurrence of a subtstring, if not found returns -1
print(challenge.rfind("n")) # Return the index of the last occurrence of a substring, if not found returns -1
print(challenge.index("days")) # Return the lowest index of a substring if substring is not founded it raises a valueError
print(challenge.rindex("days")) # Return the highest index of a substring if substring is not founded it raises a valueError
challenge3 = "thirtydaysofpython"
print(challenge3.isalnum()) # Checks if all string elements contains just alphanumeric characters (space, ",", ".", are not one)
print(challenge3.isalpha()) # Checks if all string elements are alphabet characteres (space is not allowed again)
print(challenge3.isdecimal()) # Check if all characters in a astring are decimal (0-9)
print(challenge3.isdigit()) # Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
print(challenge3.isnumeric()) # Checks if all characters in a string are numbers or number related
print(challenge3.isidentifier()) # Checks if a string is a valid variable name
print(challenge3.islower()) # Checks if all alphabet characters in a string are lowercase
print(challenge3.isupper()) # Checks if all alphabet characters in a string are uppercase
web_tech = ["HTML", "CSS", "JS", "REACT"]
result = "," # A comma between each element of the list
print(result.join(web_tech)) # Returns a concatenated string
print(challenge.strip("noth")) # Removes all given characters starting from the beginning and end of the string
print(challenge.replace("python", "javascript")) # Replaces substring with a given string
print(challenge.split()) # Splits the string, using given string or space as a separator
print(challenge.title()) # Return a tittle cased string
print(challenge.swapcase()) # Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
print(challenge.startswith("thirty")) # Checks if String Starts with the Specified String (case sensitive)
