def retorna_a_soma_dos_numeros_pares_de_uma_lista(lista):

    lista_de_valores_pares = list()


    for valor in lista:


        lista_de_valores_pares.append(valor) if valor % 2 == 0 else '' 


    print(lista_de_valores_pares)


    return [lista_de_valores_pares, sum(lista_de_valores_pares)]