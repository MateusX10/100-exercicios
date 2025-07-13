from funcs import *
from random import randint



lista = [randint(0, 40) for valor in range(0, randint(3, 50))]


linha()
print(f"Lista gerada: {lista}")
linha()

quebra_linha()


resposta = verifica_se_ha_elementos_duplicados_na_lista(lista)


print(resposta)