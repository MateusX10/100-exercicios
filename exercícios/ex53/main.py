# algoritmo de ordenação Bubble Sort



lista = [5, 3, 8, 4]



ciclos = 0



while ciclos < 3:


    for posicao, item in enumerate(lista):


        if posicao < (len(lista) - 1):

            if lista[posicao] > lista[posicao + 1]:


                temp = lista[posicao]

                lista[posicao] = lista[posicao + 1]

                lista[posicao + 1] = temp



    ciclos += 1    


print(lista)


