from funcs import *
from random import randint



opcoes_validas = [1, 2, 3]


options = ["pedra", "papel", "tesoura"]


continuar = True



pontuacao = {"computador": 0, "jogador": 0}


opcao_escolhida_pelo_jogador = ''


while continuar:


    jogada_computador = options[randint(0, 2)]


    opcoes()



    while True:


        escolha_usuario = int(input("Você irá de? "))


        if escolha_usuario in opcoes_validas:

            break

        print("\033[1;31mOpção inválida. Por favor, tente novamente.\033[1;31m")


    jogada_jogador = options[escolha_usuario - 1]



    print(f"Jogador: {jogada_jogador}")

    print(f"Computador: {jogada_computador}")

    if jogada_jogador == "pedra":

        
        
        if jogada_computador == "pedra":

            print("EMPATE!")

            pontuacao["jogador"] += 1

            pontuacao["computador"] += 1


        elif jogada_computador == "papel":

            print("COMPUTADOR VENCEU!")


            pontuacao["computador"] += 1


        elif jogada_computador == "tesoura":


            print("JOGADOR VENCEU!")


            pontuacao["jogador"] += 1


    elif jogada_jogador == "papel":


        if jogada_computador == "pedra":


            print("JOGADOR VENCEU!")

            
            pontuacao["jogador"] += 1


        elif jogada_computador == "papel":


            print("EMPATE!")


            pontuacao["jogador"] += 1
            pontuacao["computador"] += 1


        elif jogada_computador == "tesoura":


            print("COMPUTADOR VENCEU")

            pontuacao["computador"] += 1


    elif jogada_jogador == "tesoura":


        
        if jogada_computador == "pedra":

            print("COMPUTADOR VENCEU!")

            pontuacao["computador"] += 1


        elif jogada_computador == "papel":


            print("JOGADOR VENCEU!")

            pontuacao["jogador"] += 1


        elif jogada_computador == "tesoura":


            print("EMPATE!")


            pontuacao["jogador"] += 1

            pontuacao["computador"] += 1

    

   
    


    while True:


        continuar_ou_nao = str(input("Continuar? [S/N]")).strip().upper()[0]


        if continuar_ou_nao in "SN":

            break

        print("\033[1;31mOpção inválida. Por favor, tente novamente.\033[m")



    if continuar_ou_nao == "N":

        continuar = False


linha()
print(f'Pontuação:')


if pontuacao["jogador"] > pontuacao["computador"]:

    print(f"1º Jogador - {pontuacao['jogador']} pontos")
    print(f"2º Computador - {pontuacao['computador']} pontos")

elif pontuacao["computador"] > pontuacao["jogador"]:

    print(f"1º Computador - {pontuacao['computador']} pontos")
    print(f"2º Jogador - {pontuacao['jogador']} pontos")

else:

    print(f"1º Computador - {pontuacao['computador']} pontos")
    print(f"1º Jogador - {pontuacao['jogador']} pontos")

linha()
