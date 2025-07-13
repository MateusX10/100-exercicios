maior = menor = 0


numeros_informados = []



continuar = True


while continuar:

    for contador in range(0, 10):

        valor = int(input(f"{contador + 1}º valor: "))

        if valor > maior:

            maior = valor

        if valor < menor or contador == 0:

            menor = valor

        numeros_informados.append(valor)



    print(f"Dentre os números: ", end='')


    for numero in numeros_informados:


        print(f"{numero}, ", end='')



    print(f"\nO maior número informado foi {maior} e o menor foi {menor}")


    numeros_informados.clear()



    while True:


        continuar_ou_nao = str(input("Continuar [S/N]? ")).strip().upper()[0]


        if continuar_ou_nao in "Nn":

            continuar = False



        break
