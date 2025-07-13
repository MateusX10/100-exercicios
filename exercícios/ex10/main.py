from funcs import *



numero = int(input("Digite um número para verificar se ele é palíndromo: "))


numero_e_palindromo = verifica_se_um_numero_e_palindromo(numero)


if numero_e_palindromo:

    print(f"{numero} é palíndromo")

else:

    print(f"{numero} não é palíndromo")