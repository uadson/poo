from random import randint, choice
from string import ascii_letters


# sem list_comprehension

lista = []

# iteração de um valor para preenchimento da lista

for i in range(10):
    lista.append(str(i))

print(lista)

"""
OUTPUT:
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
"""

# com list_comprehension

"""
1. Objetivo:
    criar uma lista com strings de números de 0 a 9:
    [] - o mesmo que: lista = []

2. Objeto responsavel por implementar a lista
    str(i)
"""
#Logo:

print([str(i) for i in range(10)])

"""
OUTPUT
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
"""
letras = ascii_letters
letras_aleatorias = ''.join(choice(letras) for _ in range(4))

print(letras_aleatorias)

"""
OUTPUT
TVJR
"""