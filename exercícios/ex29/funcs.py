def calcula_fatorial_de_um_numero(numero):


    f = 1
    

    print(f"{numero}! = ", end='')

    for valor_antecessor in range(numero, 0, -1):

        
        f *= valor_antecessor


        print(f"{valor_antecessor} x " if valor_antecessor != 1 else f"{valor_antecessor} = ", end='')




    return f