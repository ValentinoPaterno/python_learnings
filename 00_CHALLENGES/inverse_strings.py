"""
Crear un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma
automatica.
Ej: Si le pasamos "hola mundo" -> "odnum aloh"
"""
def reversed_str(string: str ) -> str:
    """ Function that receive a str and reverse it"""
    new_str = ""
    for i in range(len(string) - 1, -1, -1):
        new_str = new_str + string[i]
    return new_str
print(reversed_str("Hola mundo"))
