def remove_elementos_duplicados(lista):


    elementos_que_ja_apareceram = list()



    for elemento in lista:

        if elemento not in elementos_que_ja_apareceram:

            elementos_que_ja_apareceram.append(elemento)


        else:

            lista.remove(elemento)



    return elementos_que_ja_apareceram