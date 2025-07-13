def zip2(lista1, lista2):

    
    listas_combinadas = []


    if len(lista1) > len(lista2):

        lista1 = lista1[0:len(lista2)]

    elif len(lista2) > len(lista1):

        lista2 = lista2[0:len(lista1)]



    for posicao in range(0, len(lista1)):

        listas_combinadas.append((lista1[posicao], lista2[posicao]))


    return listas_combinadas