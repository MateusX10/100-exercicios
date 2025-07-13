from funcs import linha
from random import choice


palavras = ["foca", "raposa", "madeira", "estudar",
            "cama", "ilha", "casa", "pessoa",
            "almofada", "nuvem", "sol", "lua",
            "computador", "internet", "unha"]



numero_de_erros_permitidos = 6

erros_cometidos_pelo_usuario =  letras_ainda_nao_acertadas = 0


usuario_acertou_a_palavra = False


letras_chutadas_pelo_usuario = []


palavra_escolhida = choice(palavras)


while erros_cometidos_pelo_usuario < numero_de_erros_permitidos and not usuario_acertou_a_palavra:




    
    for letra in palavra_escolhida:

        print('_ ' if letra not in letras_chutadas_pelo_usuario else letra, end='')


    print(f"\nLetras chutadas: {letras_chutadas_pelo_usuario}\n")
    
    letra_chutada_pelo_usuario = str(input("Chute uma letra:  "))

    letras_chutadas_pelo_usuario.append(letra_chutada_pelo_usuario)


    for letra in palavra_escolhida:

        if letra not in letras_chutadas_pelo_usuario:

            letras_ainda_nao_acertadas += 1


    
    if letras_ainda_nao_acertadas == 0:

        usuario_acertou_a_palavra = True

    else:

        if letra_chutada_pelo_usuario not in palavra_escolhida:

            erros_cometidos_pelo_usuario += 1


    letras_ainda_nao_acertadas = 0


if usuario_acertou_a_palavra:
    print("Você acertou a palavra!")

else:

    print("\033[1;31mVocê errou a palavra.\033[m")    


linha()
print(f"Palavra: {palavra_escolhida}")
print(f"Erros: {erros_cometidos_pelo_usuario}")
linha()