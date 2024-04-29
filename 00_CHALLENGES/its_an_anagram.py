"""
Escribir una función que reciba DOS palabras y retorne verdadero o falso
segun sean o no anagramas
-   Un anagrama consiste en formar una palabra reordenando TODAS las letras
    de otra palabra inicial
-   NO hace falta comprobar que AMBAS palabras existan.
-   DOS palabras EXACTAMENTE iguales NO SON ANAGRAMA.
"""
def its_anagram(word1: str, word2: str) -> bool:
    if word1.lower() == word2.lower:
        return False
    print(sorted(word1.lower()))
    print(sorted(word2.lower()))
    return sorted(word1.lower()) == sorted(word2.lower())



print(its_anagram("amor","romaa"))