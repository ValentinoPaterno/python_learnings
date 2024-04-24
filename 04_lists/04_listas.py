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

# Modificando Listas -> Una lista es una coleccion ordenada de itema mutable y modificable
fruits[0] = "Avocado" # Cambio el valor de la posicion 0 por un determinado valor no importa el tipo
print(fruits)

# Buscando un item en una lista
existe_item = "Banana" in fruits
print(existe_item) # Devuelve True si se encuentra el item en la lista

# Añadiendo items a una lista con el método append().
fruits.append("Sandia") # Este método siempre agrega al final de la lista
print(fruits)

# Insertando items a traves de metodo insert()
fruits.insert(1, "Pinnaple") # Recibe 2 parametros: index donde inserta el elemento y el elemento
print(fruits)

# Removiendo items con el metodo remove() - Elimina la primer ocurrencia en la lista
fruits.remove("Banana") 
print(fruits)

# Removiendo un item en determinada posicion con el metodo pop()
fruits.pop(0) # Eliminará el item en la posicion 0, es decir "Avocado"
print(fruits) # Si no se especifica el index, elimina el ultimo item.

# Removiendo un item o la lista con la palabra clave "Del"
del fruits[0]
print(fruits)
del fruits 
# print (fruits)  devuelve error ya que eliminé la lista

# Dejando vacia una lista (no eliminarla) mediante el metodo clear()
new_list = ["exp1", "exp2", "exp3"]
new_list.clear()
print(new_list) # retorna -> []

# Copiando una lista con el metodo copy(). Se puede copiar una lista haciendo list1 = list2 ; pero sin embargo esto puede causar problemas ya que list1 es una referencia para list2, entonces cualquier cambio en list1 puede afectar a list2, para evitar eso es que se utiliza el metodo copy() 

animals = ["cat", "dog", "jiraffe"]
animals_copy = animals.copy()
print(animals_copy)

# Uniendo o concatenando 2 listas distintas
    # + operator
birds = ["Eagle", "Duck", "Crow", "Geese"]
result_list = animals + birds
print(result_list)
    # Usando el metodo extend(), este metodo añade una lista a otra, es decir modifica la misma
animals.extend(birds)
print("Estos son animales:", animals)

# Contando la cantidad de elementos de una lista con count(), este metodo cuenta la cantidad de veces que se repite un elemento en una lista
animals.append("Eagle")
cant_repetida = animals.count("Eagle")
print(cant_repetida)

# Encontrando la posicion en la primer coincidencia de determinado elemento con el metodo index(),
print(animals.index("Eagle"))

# Revirtiendo el orden de una lista con el metodo reverse()
animals.reverse()
print(animals)

# Ordenando una lista con el metodo sort(), modificando la lista origianl, si el argumento reverse=true, se ordena en orden descendente
animals.sort()
print(animals)
animals.sort(reverse=True)
    # sorted() es una built-in function de python, devuelve otra lista sin modificar la lista original
animals_sorted = sorted(animals, reverse=True) #ejemplo con orden inverso incluido
print(animals_sorted)

# ----------------------- Ejercicios ----------------------------
empty_list = []
five_items_list = [1,2,3,4,5]
print(len(five_items_list))
mid_element = int(len(five_items_list) / 2)
print(five_items_list[0], five_items_list[-1], five_items_list[mid_element])
mixed_data_types = ["vale", 20, 1.70, "single", "Bolivar 274"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[-1], it_companies[int(len(it_companies)/2)])
it_companies[0] = "Mercado Libre"
print(it_companies)
it_companies.append("Tesla")
print(it_companies)
it_companies[3] = it_companies[3].upper()
print(it_companies)
it_companies.insert(int(len(it_companies)/2), "X")
print("#;".join(it_companies))
existe_item = "Google" in it_companies
print(existe_item)
it_companies.sort()
it_companies.reverse()
print(it_companies)
first_three_companies = it_companies[0:3]
print(first_three_companies)
last_three_companies = it_companies[6:9]
print(last_three_companies)
