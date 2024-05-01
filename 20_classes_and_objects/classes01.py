"""
Python is an object oriented programming language.
We create class to create an object. 
A class is like an object constructor, or a "blueprint" for creating objects.
We instantiate a class to create an object. 
The class defines attributes and the behavior of the object, while the object, 
on the other hand, represents the class.
"""

# Creating Classes

# class Person:
#     pass
# print(Person)

# Creating an object - We can create an objetc by calling the class

# p = Person()
# print(p)

# Class Constructor - A class without a constructor is not useful. We use
# init() constructor function, this function has a self parameter which
# is a reference to the current instance of the class

# class Person:
#     def __init__(self, firstname, lastname, age, country, city):
#         # self allows to attach parameter to the class
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.country = country
#         self.city = city

# p = Person("valentino", "paterno", 20, "argentina", "corrientes")
# print(p.firstname, p.lastname, p.age ,p.country, p.city)

# Object Methods

# class Person:
#     def __init__(self, name, surname, age, country, city):
#         self.name = name
#         self.surname = surname
#         self.age = age 
#         self.country = country 
#         self.city = city 
#     def person_info(self):
#         return f'{self.name} {self.surname} is {self.age} years old. He lives in {self.city}, {self.country}'

# p = Person('valentino', 'paterno', 20, 'argentina', 'corrientes')
# print(p.person_info())

# Object Default Methods -> Sometimes you may want to have a default values for objetc methods.
# If we give default values for the parameters in the constructor, we can avoid errors when we
# call or instantiate our class without parameters. 

class Person:
    def __init__(self, firstname='noname', lastname='nolastname', age=0, country='null', city='null'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

# p1 = Person()
# print(p1.person_info())
# p2 = Person('Valentino', 'Paterno', 20, 'Corrientes', 'Argentina')
# print(p2.person_info())

# Method to modify Class default values

# class Human:
#     def __init__(self, name="Valentino", age=20, country="Argentina"):
#         self.name = name 
#         self.age = age 
#         self.country = country
#         self.skills = []
#     def info(self):
#         return f'Name: {self.name}\nAge: {self.age}\nCountry: {self.country}'
#     def add_skill(self,skill):
#         self.skills.append(skill)

# h1 = Human("sandra", "53", "argentina")
# h1.add_skill("hardworker")
# print(h1.info())
# print(h1.skills)

# Iheritance - We can reuse parent class code. Allows us to define a class that inherits
# all the methods and properties from parent class. The parent class is which gives all
# the methods and properties. Child class is the class that inherits from another parent

# class Student(Human):
#     pass 

# student_one = Student("valentino", 20, "argentina")
# student_one.add_skill("python") 
# print(f"--- Student info ---\n{student_one.info()}\nSkills: {student_one.skills}")

# Now calling the init() constructor, to acces the parent properties by calling super
# We can add a new method to the child class
# When we add the init() constructor, the child class will no longer inherit the 
# parent's init() function.

# class Student(Person):
#     def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
#         self.gender = gender
#         super().__init__(firstname, lastname,age, country, city)
#     def person_info(self):
#         gender = 'He' if self.gender =='male' else 'She'
#         return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

# student1 = Student("Valentino", "Paterno", 20, "Argentina", "Corrientes", "male")
# print(student1.person_info())