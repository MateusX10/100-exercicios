from classes import Stack
from funcs import *

pilha1 = Stack()


opcoes_validas = [1, 2, 3, 4, 5, 6] # push - pop - top - is_empty - size - quit


continuar = True


while continuar:


    menu()


    while True:


        escolha_usuario = int(input("Escolha uma operação: "))


        if escolha_usuario in opcoes_validas:
            

            break

        print("\033[1;31mOpção inválida. Por favor, tente novamente.\033[m")


    # push
    if escolha_usuario == 1:


        elemento_a_ser_adicionado = int(input("Elemento a ser adicionado: "))

        pilha1.push(elemento_a_ser_adicionado)
    


    # pop
    elif escolha_usuario == 2:


        pilha1.pop1()



    # top
    elif escolha_usuario == 3:


        print(pilha1.top())



    # is_empty
    elif escolha_usuario == 4:


        pilha1.is_empty()

    
    # size
    elif escolha_usuario == 5:

        print(pilha1.size())


    # quit
    else:


        continuar = False
