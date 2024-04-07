# Listas
fullNames_List = ["Valentino Paterno", "Sandra Martinez", "Paula Galarzas"]
list_user = ["Sandra", "Martinez", 53, 1970] # Una lista puede tener distintos tipos de datos
# Acceso a listas
name = list_user[0]
print(name)
anio = list_user[-1]
print(anio)
# Unpacking List Items
lst = [1, 2, 3, 4]
num_1, num_2, *rest = lst 
print(num_1,num_2,rest)
# Slicing from a List
# Positive Indexing
fruits = ["Apple", "Orange", "Banana", "Strawberrie"]
all_fruits = fruits[0:] # Slice all the elements
print(all_fruits)
# Negative Indexing
all_fruits = fruits[-4:]
print(all_fruits)
# Reverse 
all_fruits = fruits[::-1]
print(all_fruits)