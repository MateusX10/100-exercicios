def verifica_se_duas_palavras_sao_anagramas(palavra1, palavra2):

    print(sorted(palavra1))

    print(sorted(palavra2))


    if sorted(palavra1) == sorted(palavra2):

        print("positivo")


    else:

        print("negativo")