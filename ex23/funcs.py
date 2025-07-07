def gera_os_n_primeiros_valores_da_sequencia_de_fibonacci(quantidade):

    anterior = atual = novo = 0


    for valor in range(0, quantidade):




        print(f"{novo} -> " if valor + 1 != quantidade else f"{novo} -> fim" , end='')

        anterior = atual

        atual = novo

        if valor == 0:

            novo = 1

        else:

            novo = atual + anterior

        

