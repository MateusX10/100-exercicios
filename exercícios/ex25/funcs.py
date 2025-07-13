def verifica_se_uma_frase_e_um_palindromo(frase):

    return frase == frase[::-1]



def remove_espacos_de_uma_string(string):


    nova_string = string.split()


    nova_string = ''.join(nova_string)

    return nova_string