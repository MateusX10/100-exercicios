from funcs import *
import random


lista = [1, 2, 3, 4, 5, 6, 7]


lista2 = [random.randint(0, 100) for _ in range(0, 50)]

print(lista2)


print(retorna_segundo_maior_elemento_da_lista(lista2))