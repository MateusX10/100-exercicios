from funcs import *



n1 = int(input("Primeiro valor: "))

while True:


    n2 = int(input("Segundo valor: "))


    if n2 == 0:

        print("\033[1;31mOps! Não se pode dividir um número por 0... por favor, tente novamente.\033[m")

        continue


    break
print(calcula_mdc(n1, n2))