from funcs import *




minimo = 0

maximo = 1


for numero in range(1, 11):

    minimo += 1

    if minimo == maximo:

        print(f"{numero} ")

        maximo += 1

        minimo = 0

    else:

        print(f"{numero} ", end='')