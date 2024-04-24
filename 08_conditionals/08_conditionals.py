# a = 3
# if a > 0:
#     print("a es un numero positivo")

# a = -3
# if a > 0:
#     print("a es un numero positivo")
# else:
#     print("a es un numero negativo")

# a = 0 
# if a > 0:
#     print("a es un numero positivo")
# elif a < 0:
#     print("a es un numero negativo")
# else: 
#     print("a es igual a 0")

# a = -1
# # Short hand
# print("a es positivo") if a > 0 else print("a es negativo")

# # nested conditions
# if a < 0:
#     if a % 2 == 0:
#         print("a is negative and an even number")
#     else: 
#         print("a is negative and odd number")
# else:
#     print("a is positive or zero")
# # nested can be avoid using and operator
# a = -1
# if a > 0 and a % 2 == 0:
#     print("a es positivo y par")
# elif a > 0 and a % 2 != 0:
#     print("a es positivo y es impar")
# elif a == 0:
#     print("a es cero")
# else:
#     print("a es negativo")

# # using logical operator or 
# age = 16 
# guest = True
# if age > 18 or guest == True:
#     print("Acceso concedido")
# else:
#     print("Acceso denegado")
# ----------------- Ejercicios -----------------------
# age = int(input("Enter you age:"))
# if age >= 18: 
#     print("You are old enought to learn to drive.")
# else:
#     print(f"You need {18 - age} more years to learn to drive")

# my_age = 20
# your_age = int(input("Enter your age: "))
# if my_age > your_age:
#     print(f"I'm {my_age - your_age} years older than you.")
# elif my_age < your_age:
#     print(f"You're {your_age - my_age} years older than me")
# else:
#     print("We're the same age!")

# num_1 = int(input("Enter first number:"))
# num_2 = int(input("Enter second number:"))
# if (num_1 > num_2): 
#     print(f"{num_1} is greather than {num_2}")
# elif (num_1 < num_2):
#     print(f"{num_1} is smaller than {num_2}")
# else: 
#     print(f"{num_1} is equal to {num_2}")

# score = int(input("Enter your score: "))
# if 0 <= score <= 49:
#     print("Your grade is F")
# elif 50 <= score <= 59:
#     print("Your grade is D")
# elif 60 <= score <= 69:
#     print("Your grade is C")
# elif 70 <= score <= 89:
#     print("Your grade is B")
# elif 90 <= score <= 100:
#     print("Your grade is A")
# else:
#     print("Your score is unvailable.")

# month = input("Enter the month: ").lower()

# if month == ("september" or "october" or "november"):
#     print("The season which you're in is Autumn.")
# elif month == ("december" or "january" or "february"):
#     print("The season which you're in is Winter.")
# elif month == ("march" or "april" or "may"):
#     print("The season which you're in is Spring")
# else: 
#     print("The season you're in is Summer")

# fruits = ['banana', 'orange', 'mango', 'lemon']
# new_fruit = input("Enter the new fruit to add to the list: ")

# if fruits.count(new_fruit) > 0:
#     print("The fruit already exits in the list.")
# else: 
#     fruits.append(new_fruit)

# print(fruits)

# Level 3
# person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'MongoDB', 'Python', "Node"],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }
# if person.get("skills") is not None:
#     skills = person.get("skills")
#     print(f"The middle skill is: {skills[int(len(skills)/2)]}")
#     print("Person has Python in their skills") if "Python" in skills else print("Person hasn't got Python in their skills")
    
#     skills = set(skills)
#     set_skills = {"JavaScript", "React", "MongoDB", "Python", "Node"}
#     if (set_skills.intersection(skills) == set_skills):
#         print("He's a full stack developer")
#     elif (set_skills.intersection(skills) == {"MongoDB", "Python", "Node"}):
#         print("He's a backend developer")
#     elif (set_skills.intersection(skills) == {"React", "JavaScript"}):
#         print("He's a frontend developer")
#     else:
#         print("Unknown tittle.")
# else: 
#     print("Person hasn't skills")

# first_name = person.get("first_name")
# last_name = person.get("last_name")
# print (f"{first_name} {last_name} lives in Finland. He's married") if person.get("is_married") == True and person.get("country") == "Finland" else print("Not married")

