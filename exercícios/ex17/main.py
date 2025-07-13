from funcs import *




valor_da_medida_a_ser_convertida = 0


continuar = True

while continuar:

    mostra_menu()


    while True:

        escolha_usuario = int(input("Sua escolha: "))

        if escolha_usuario in [1, 2]:

            break

        print("\033[1;31mOpção inválida. Tente novamente.\033[m")



    valor_da_medida_a_ser_convertida = int(input("Valor da medida a ser convertida: "))


    if escolha_usuario == 1:

        print("Celsius -> fahrenheit")


        converte_para_fahrenheit(valor_da_medida_a_ser_convertida)

    else:



        print("Fahrenheit -> celsius")


        converte_para_celsius(valor_da_medida_a_ser_convertida)


    while True:


        continuar_ou_nao = str(input("Continuar [S/N]? ")).strip().upper()[0]

        if continuar_ou_nao in "Nn":

            continuar = False


        break


