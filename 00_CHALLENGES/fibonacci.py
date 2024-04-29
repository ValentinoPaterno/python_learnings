"""
Escribir un programa que imprima los 50 primeros numeros de la sucesion
de fibonacci empezando en 0.
- la serie fibonacci se compone por una suecesion de numeros en la que
el siguiente siempre es la suma de los dos anteriores
0,1,1,2,3,5,8,13,...
"""
def fibonacci_sucesion():
    """Function that returns a list with fibonacci sucesion"""
    lst = []
    first_ant = 1
    second_ant = 0
    resul = 0
    for i in range (0,49):
        if not lst:
            lst.append(second_ant)
            lst.append(first_ant)
        else:
            resul = first_ant + second_ant
            lst.append(resul)
            second_ant = first_ant
            first_ant = resul
    print(lst)
    print(len(lst))
fibonacci_sucesion()
