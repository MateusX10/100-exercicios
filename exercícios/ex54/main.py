lista = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]


lista.sort()

elemento_a_buscar = 91



copia_lista = lista[:]


fim = False



while not fim:


    elemento_do_meio = len(copia_lista) // 2

    if elemento_a_buscar == copia_lista[elemento_do_meio]:

        indice = lista.index(elemento_a_buscar)

        print(f"Valor {elemento_a_buscar} encontrado no índice {indice}")

        fim = True
        continue
    
    if len(copia_lista) == 1:


        indice = lista.index(copia_lista[0])

        print(f"Valor que restou: {copia_lista[0]}, índice: {indice}")

        fim = True

        continue

    elif elemento_a_buscar < copia_lista[elemento_do_meio]:


        copia_lista = copia_lista[0:elemento_do_meio]
    

    elif elemento_a_buscar > copia_lista[elemento_do_meio]:

        copia_lista = copia_lista[elemento_do_meio + 1:]

    #print(lista[elemento_do_meio])
