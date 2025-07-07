from funcs import *


frase = str(input("Frase: "))


frase_sem_espacos = remove_espacos_de_uma_string(frase)


print(verifica_se_uma_frase_e_um_palindromo(frase_sem_espacos))
