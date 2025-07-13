def retorna_segundo_maior_elemento_da_lista(lista):

    maior = segundo_maior = 0

    for indice, elemento in enumerate(lista):

        if indice == 0:

            maior = elemento

        elif elemento > maior:

            maior = elemento


    lista.remove(maior)

        
    for indice, elemento in enumerate(lista):

        if indice == 0:

            segundo_maior = elemento


        elif elemento > segundo_maior:

            segundo_maior = elemento


    return segundo_maior

