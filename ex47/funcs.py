def verifica_se_ha_elementos_duplicados_na_lista(lista):


    elementos_duplicados = {}

    quantidade_elementos_duplicados = 0

    elementos_ja_analisados = []

    for elemento in lista:

        if elemento  not in elementos_ja_analisados:

            if lista.count(elemento) > 1:


                elementos_duplicados[elemento] = lista.count(elemento)

                quantidade_elementos_duplicados += 1


    if quantidade_elementos_duplicados == 0:

        return "Não há elementos duplicados na lista"
    
    else:

        return f'Há um total de {quantidade_elementos_duplicados} elementos duplicados na lista, entre eles: {elementos_duplicados}'''



    

def linha():

    print("-=" * 30)


def quebra_linha():

    print("\n")