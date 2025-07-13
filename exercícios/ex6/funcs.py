def imprime_os_20_primeiros_numeros_impares()-> None:


    for numero_impar in range(1, 40, 2):

        print(f"{numero_impar}, " if numero_impar != 39 else f"{numero_impar}.", end='') 

