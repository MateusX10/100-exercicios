def encontra_o_valor_mais_frequente_em_uma_lista(lista):

    maior = 0
    valor_mais_frequente = list()


    for valor in lista:


        frequencia_palavra = lista.count(valor)


        if frequencia_palavra > maior:


            maior = frequencia_palavra


            valor_mais_frequente.clear()

            valor_mais_frequente.append(valor)

        elif frequencia_palavra == maior:

            valor_mais_frequente.append(valor)

    
    valor_mais_frequente = set(valor_mais_frequente)

    return [valor_mais_frequente, maior]