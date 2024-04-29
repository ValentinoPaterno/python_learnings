"""
Escribir un programa que se encargue de comprobar si un numero es o no primo.
Hecho esto, imprimir los numeros primos entre 1 y 100
"""
def prime_number(number: int) -> bool:
    """ Function that verify is a number is prime"""
    if number <= 1:
        return False
    divisores = 0
    for i in range (1,number+1):
        if number % i == 0:
            divisores += 1
            if divisores > 2:
                return False
    return True

for i in range(1,101):
    if prime_number(i):
        print("Primo: ",i)
    else:
        print("No primo", i)
