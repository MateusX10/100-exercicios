from funcs import *


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


lista2 = [5, 3, 9, 10, 12, 20, 2]


lista_com_elementos_em_comum = verifica_se_duas_listas_tem_elementos_em_comum(lista1, lista2)


for item in lista_com_elementos_em_comum:

    print(f"{item} - ", end='')
