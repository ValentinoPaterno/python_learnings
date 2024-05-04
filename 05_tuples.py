my_tuple = () # Conjunto de valores ordenados inmutables los cuales no pueden ser cambiados una vez creados
my_tuple = (20, 1.70, "Valentino", "Paterno")
# my_tuple[0] = 30 --> Esto devuelve un error
length_tuple = len(my_tuple)
first_item = my_tuple[0] # Al igual que en las listas las tuplas estan indexadas
sub_tuple = my_tuple[0:3] # Slice de tupla con los 3 primeros elementos 
"""Si queremos modificar un valor de una tupla debemos previamente cambiarla a lista y despue"""
# my_tuple = list(my_tuple)
# my_tuple[0]= 50
# print(my_tuple)
print(20 in my_tuple) # Utilizaciono operador in para conocer existencia de determiando elemento dentro de una tupla
