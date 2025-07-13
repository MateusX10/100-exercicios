def verifica_se_duas_listas_tem_elementos_em_comum(lista1, lista2):


    itens_em_comum = []

    for item in lista1:

        if item in lista2:

            itens_em_comum.append(item)
            

    return itens_em_comum