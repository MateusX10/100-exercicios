def exibe_a_tabuada_de_um_numero(numero: int)-> None:


    for valor in range (1, 11):

        resultado = numero * valor

        print(f"{numero} x {valor} = {resultado}")