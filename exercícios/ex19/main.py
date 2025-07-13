from funcs import *



continuar = True


opcoes_de_operacoes_matematicas_possiveis = [1, 2, 3, 4]

while continuar:


    mostra_menu()


    while True:

        operacao_escolhida = int(input("Escolha uma operação: "))

        if operacao_escolhida in opcoes_de_operacoes_matematicas_possiveis:

            break

        print("\033[1;31mOpção matemática inválida. Por favor, tente novamente.\033[m")



    n1 = int(input("Valor 1: "))

    n2 = int(input("Valor 2: "))


    if operacao_escolhida == 1:


        resultado = adicao(n1, n2)

        print(f"{n1} + {n2} = {resultado}")


    elif operacao_escolhida == 2:


        resultado = subtracao(n1, n2)


        print(f"{n1} - {n2} = {resultado}")


    
    elif operacao_escolhida == 3:

        resultado = multiplicacao(n1, n2)


        print(f"{n1} x {n2} = {resultado}")


    else:


        resultado = divisao(n1, n2)

        print(f"{n1} / {n2} = {resultado}")



    while True:


        continuar_ou_nao = str(input("Continuar [S/N]? ")).strip().upper()[0]


        if continuar_ou_nao in "Nn":

            continuar =  False

        break