from random import randint




continuar = True

while continuar:

    print("Vou pensar em um número entre 0 a 10... vamos ver se consegue adivinhar qual é!!!")

    numero_pensado_pelo_computador = randint(0,10)

    while True:

        palpite_do_jogador = int(input("Qual o seu palpite? "))


        if palpite_do_jogador == numero_pensado_pelo_computador:

            print(f"Parabéns! Você acertou! Eu de fato pensei no número {numero_pensado_pelo_computador}")

            break

        else:
            
            if palpite_do_jogador > numero_pensado_pelo_computador:

                print("Tente chutar  um número menor")

            else:

                print("Tente chutar um número maior")


        


        

        continuar_ou_nao = str(input("Continuar? [S/N]")).strip().upper()[0]

        if continuar_ou_nao in "Nn":

            continuar = False




