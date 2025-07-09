def menu():

    print('''Menu:
[ 1 ] - Adicionar item ao inventário
[ 2 ] - Remover item do inventário
[ 3 ] - Mostrar itens
[ 4 ] - Verificar se um item existe
[ 5 ] - Atualizar a quantidade de um item
[ 6 ] - Sair
          ''')
    

def linha(tamanho_da_linha=30):


    print("-=" * tamanho_da_linha)


def titulo(texto):


    tamanho_do_texto = len(texto) + 4


    linha(tamanho_do_texto)
    print(texto.center(tamanho_do_texto))
    linha(tamanho_do_texto)