def calcula_subtracao_com_divisao_sucessiva(dividendo, divisor):

    quantidade_de_vezes_subtraidas = 0

    result = dividendo


    while result > 0:


        result -= divisor


        print(f"{dividendo} - {divisor} = {result}")

        dividendo = result


        quantidade_de_vezes_subtraidas += 1



    return quantidade_de_vezes_subtraidas