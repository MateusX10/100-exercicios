def inverte_uma_lista(lista):

    #lista.reverse()

    #return lista[::-1]


    lista_invertida = list()

    for item in range(len(lista) - 1, -1, -1):

        lista_invertida.append(lista[item])


    return lista_invertida

