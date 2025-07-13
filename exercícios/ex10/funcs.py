def verifica_se_um_numero_e_palindromo(numero: int)-> bool:



    numero = str(numero)


    return numero == numero[::-1]