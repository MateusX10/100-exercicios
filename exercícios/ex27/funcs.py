def verifica_se_um_numero_e_perfeito(numero):
    


    soma = 0

    for valor in range(1, numero):

        
        if numero % valor == 0:

            soma += valor


    return soma == numero