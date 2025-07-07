def verifica_se_um_numero_e_primo(numero: int)-> bool:

    numero_e_primo = False

    for valor_antescessor in range(2, numero):

        if numero % valor_antescessor == 0:

            numero_e_primo = True

    return numero_e_primo