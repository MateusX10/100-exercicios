from funcs import *
from random import randint


lista1 = [randint(0, 100) for contador in range(0, randint(1, 11))]

lista2 = [randint(0, 100) for contador in range(0, randint(1, 11))]


nova_lista = junta_duas_listas_e_as_intercala(lista1, lista2)


print(nova_lista)