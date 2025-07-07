def conta_quantos_multiplos_de_3_existem_entre_1_e_1000()->None:


    contador = 3


    valores_totais_multiplos_de_3 = 1

    
    while contador <= 1000:


        
        if contador % 3 == 0:

            valores_totais_multiplos_de_3 += 1


        contador += 3


    print(valores_totais_multiplos_de_3)