from funcs import *


n1 = float(input("Digite um valor: "))

n2 = float(input("Digite outro valor: "))


n3 = float(input("Digite mais um valor: "))


media = calcula_a_media_de_varios_valores(n1, n2, n3)


print(f"A média entre os valores {n1}, {n2} e {n3} é {media:.2f}")