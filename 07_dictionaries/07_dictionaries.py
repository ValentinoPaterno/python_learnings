# Un diccionario es una coleccion desordenada, modificable (mutable) con un tipo de dato paired -> key: value
# Almacena todo tipo de datos
empty_dict = {}
person = {
    "first_name": "Valentino",
    "last_name": "Paterno",
    "skills": ["Python"],
    "age": 20
}
len(person) # Muestra la cantidad pares key:value en el diccionario
print(person["first_name"]) # Podemos acceder a un valor mediante la key
# Acceder a un valor mediante la key puede arrojar un error si la key no existe.
# Para evitar dicho error se utiliza el metodo get() que retorna None que es un tipo de dato NoneType si la clave no existe.
print(person.get("first_name"))
print(person.get("age"))
print(person.get("adress"))
# Para agregar items a un diccionario lo hacemos agregando la key y el value
person["adress"] = "Bolivar 108"
print(person.get("adress"))
person["skills"].append("JS") 
print(person)
# Modificando items de un diccionario
person["adress"] = "Tucuman 2020"
# Verificando existencia de claves 
print("adress" in person)
print("hobbies" in person)
# Removiendo Key and Value de un diccionario
    # pop(key): remueve el item con determinado clave:
    # popitem(): remueve el utlimo item
    # del: remueve un item con una determinada clave
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
# Cambiando de diccionario a una lista de items (lista de tuplas)
print(person.items()) # Imprime las parejas de key and value como una lista de tuplas
# Podemos conseguir una lista de las Keys de un diccionario con el metodo keys()
lista_keys = person.keys() 
print(lista_keys)
# Podemos conseguir una lista de los valores de un diccionario con el metodo values()
lista_values = person.values()
print(lista_values)
# Copiando un diccionario 
person_copy = person.copy()
# Borrando un diccionario
del person
# Dejando vacio un diccionario
person_copy.clear()

print("----------- Ejercicios -----------")
dog = {
    "name":"Lucho",
    "breed": "Mongrel",
    "legs": 4,
    "age":14
}
student = {
    "first_name": "Valentino",
    "last_name": "Paterno",
    "gender": "Male",
    "marital-status": "Single",
    "skills": ["Python", "MongoDB", "Linux"],
    "country": "Argentina",
    "city": "Corrientes",
    "address": {
        "street": "Bolivar",
        "number": 274
    }
}
print(len(student))
skills = student.get("skills")
print(type(skills))
student["skills"].append("MySQL")
student["skills"].append("Docker")
print(student["skills"])
student_list_keys = student.keys()
student_list_values = student.values()
student_list = student.items()
print(student_list)
student.pop("marital-status")
print(student)
del student