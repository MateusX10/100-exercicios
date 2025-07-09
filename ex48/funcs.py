def devolve_a_soma_acumulada_de_uma_lista(lista):

    tamanho_da_lista = len(lista) + 1 


    lista_acumulada = list()


    for posicao in range(1, tamanho_da_lista):

        lista_acumulada.append(sum(lista[0:posicao]))


    print(f"Lista acumulada: {lista_acumulada}")




def linha():

    print("-=" * 30)



def quebra_linha():


    print("\n")