from funcs import *
from random import randint

lista = [randint(0, 10) for contador in range(0, randint(5, 30))]


#lista = [4, 5, 6, 7]

linha()

print(f"Lista gerada: {lista}")

linha()


quebra_linha()

devolve_a_soma_acumulada_de_uma_lista(lista)