from funcs import *


numero = int(input("Digite um valor: "))


numero_e_par = verifica_se_um_numero_e_par_ou_impar(numero)


if numero_e_par:

    print(f"\033[1;32m{numero} é par\033[m")


else:

    print(f"\033[1;31m{numero} não é par\033[m")