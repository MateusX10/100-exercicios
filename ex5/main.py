from funcs import *



numero = int(input("Digite um número: "))


numero_e_primo = verifica_se_um_numero_e_primo(numero)

if numero_e_primo:

    print(f"{numero} é primo")

else:

    print(f"{numero} não é primo")