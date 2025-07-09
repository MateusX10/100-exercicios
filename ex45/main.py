from funcs import *
from random import randint



lista = [randint(0, 100) for valor in range(0, randint(3, 20))]


print(f"Lista completa: {lista}")


print(f"Soma dos valores da lista completa: {sum(lista)}")


valores_pares_da_lista = retorna_a_soma_dos_numeros_pares_de_uma_lista(lista)


print(f"Lista com apenas os valores pares: {valores_pares_da_lista[0]}")


print(f"Lista com a soma dos valores pares: {valores_pares_da_lista[1]}")