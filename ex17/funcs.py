def mostra_menu():

    print('''\nEscolha uma conversão:\n[ 1 ] - Celsius -> Fahrenheit
[ 2 ] - Fahrenheit -> Celsius 
          ''')


def converte_para_fahrenheit(medida_em_celsius):


    calculo = (medida_em_celsius * 9/5) + 32


    resultado_da_conversao = calculo


    print(resultado_da_conversao)



def converte_para_celsius(medida_em_fahrenheit):

    calculo = (medida_em_fahrenheit - 32) * 5/9


    resultado_da_conversao = calculo


    print(resultado_da_conversao)


