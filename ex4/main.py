from funcs import *


ano = int(input("Digite um ano: "))


ano_e_bissexto = verifica_se_um_ano_e_bissexto(ano)

if ano_e_bissexto:

    print(f"{ano} é bissexto")

else:

    print(f"{ano} não é bissexto")