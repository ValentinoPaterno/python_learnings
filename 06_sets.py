""" Set es una coleccion de items desordenados y no indexados distintos de si. Se usa esta estructura en Python para almacenar items unicos y es posible encontrar la union, interseccion, diferencia, etc... entre sets. """
st = set()
st1 = {"banana", "manzana", "piña", "sandia"}
LENGHT = len(st1)
# Para checkear si exise un item en en un set usamos in
# print("Existe item1 en el set?", "item1", "item1" in st1)
# Una vez que se creo un set, no se pueden cambiar sus items pero si agregar
st1.add("pera") # Agrego un solo elemento
st1.update(["frutilla","melon"]) # Agrego pasando como argumento una Lista
st1.remove("frutilla")  # Remove() remueve el elemento deseado, si no se encuentra devuelve error, metodo discard() no devuelve errores 
removed_element = st1.pop() # pop() remueve un item del set y lo retorna
st1.clear() # clear() deja vacio el set
del st1 # del elimina el set
names = ["Pedro", "Raul", "Raul", "Lorenzo", "Eucebio"]
set_names = set(names)  # Podemos convertir una lista a un set, y un set a una lista
                        # Al hacer esto, se eliminan los duplicados
st1 = {1, 2, 3, 4}
st2 = {1, 2, 3, 4, 5, 6}
st3 = st1.union(st2) # union() retorna un nuevo set
st1.update(st2) # update() inserta a un set otro set pasado como argumento
st1 = {1, 2, 3, 4, 9}
st2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
intersect = st2.intersection(st1) # intersection retorna un set de items compartidos entre 2 sets
super_s = {1,2,3,4,5}
sub_s = {1,2}
print(super_s.issuperset(sub_s)) # super_s es super set de sub_s
print(sub_s.issubset(super_s)) # sub_s es sub set de super_s
print(super_s.difference(sub_s))
print(sub_s.difference(super_s))
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9} # isdisjoin() verifica si existen items compartidos entre dos sets
even_numbers.isdisjoint(odd_numbers) # devuelve True, porque no tienen items en comun

