from funcs import *



lista = [1, 1,3, 4, 4,  5, 3, 3, 10, 10,10, 10,  10, 20, 15, 2, 1, 4, 3, 6, 7, 1]


resposta = encontra_o_valor_mais_frequente_em_uma_lista(lista)


valor_mais_frequente = resposta[0]

frequencia_da_palavra = resposta[1]



if len(valor_mais_frequente) > 1:

    print(f'''Os valores mais frequentes foram os valores:''')


    for valor in valor_mais_frequente:


        print(f"{valor} - ", end='')


    print(f"Com um total de {frequencia_da_palavra} ocorrências cada")


else:


    valor_mais_frequente = list(valor_mais_frequente)

    print(f'''O valor mais frequente foi o valor {valor_mais_frequente[0]} com um total
          de {frequencia_da_palavra} ocorrências''')