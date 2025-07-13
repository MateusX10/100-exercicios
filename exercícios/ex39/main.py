from funcs import *



fila = []


opcoes_validas = [1, 2, 3, 4, 5, 6]


continuar = True


while continuar:


    menu()


    while True:


        escolha_usuario = int(input("Escolha uma opção: "))


        if escolha_usuario in opcoes_validas:


            break

        print("\033[1;31mOpção inválida. Tente novamente.\033[m")


    # inserir
    if escolha_usuario == 1:


        elemento_a_ser_inserido = int(input("Elemento a ser inserido: "))

        fila.append(elemento_a_ser_inserido)


    # remover
    elif escolha_usuario == 2:

        if fila:

            fila.pop(0)

        else:

            print("\033[1;31mFila vazia!.\033[m")    

    # visualizar
    elif escolha_usuario == 3:

        if fila:

            print(fila)

        else:

            print("\033[1;31mFila vazia!.\033[m")

    
    # está vazia?
    elif escolha_usuario == 4:


        if fila:

            print("\033[1;32mNão está vazia!.\033[m")


        else:

            print("\033[1;31mVazia!.\033[m")

    
    # tamanho
    elif escolha_usuario == 5:



        if fila:

            tamanho_da_fila = len(fila)

            print(f"{tamanho_da_fila} elementos")


        else:

            print("\033[1;31mFila vazia!.\033[m")


    # sair
    elif escolha_usuario == 6:


        continuar = False