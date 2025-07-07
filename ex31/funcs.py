def conta_numero_de_ocorrencias_em_uma_lista(lista):

    quantidade_ocorrencias = 0

    elemento = int(input("Elemento: "))

    for item in lista:

        if elemento == item:

            quantidade_ocorrencias += 1


    return f"O elemento {elemento} apareceu {quantidade_ocorrencias} vezes na lista"

