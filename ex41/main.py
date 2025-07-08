from funcs import *




texto1 = '''Roberto foi ao mercado comprar pão, mas a padaria do mercado estava
           fechada. Além disso, o pão estava em falta no mercado.
'''


resposta = conta_palavras_unicas_em_um_texto(texto1)


quantidade_palavras = resposta[0]

palavras_unicas = resposta[1]


print(f'''Ao todo, tivemos {quantidade_palavras} palavras únicas no texto, das quais
          as palavras únicas eram:''')

for palavra in palavras_unicas:

    print(f"{palavra}")