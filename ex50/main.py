from carrinho import *
from funcs import menu



carrinho1 = Carrinho_de_compra()


opcoes_validas_menu = [1, 2, 3, 4, 5]


continuar = True


while continuar:


    menu()



    while True:


        escolha_usuario = int(input("Escolha uma opção: "))


        if escolha_usuario in opcoes_validas_menu:

            break

        print("\033[1;31mOpção inválida. Tente novamente.\033[m")

    

    if escolha_usuario == 1:


        item_a_ser_adicionado = str(input("Item: "))

        quantidade_do_item = int(input(f"Quantos {item_a_ser_adicionado}? "))


        carrinho1.adicionar_item(item_a_ser_adicionado, quantidade_do_item)



    elif escolha_usuario == 2:


        itens = list(carrinho1.itens_do_carrinho.keys())


        for posicao, item in enumerate(itens):

            print(f"{posicao + 1} - {item}")




        while True:


            item_a_ser_removido = int(input("Item a remover: "))


            if item_a_ser_removido in range(1, len(itens) + 1):


                break

            print("\033[1;31mOpção inválida. Por favor, tente novamente.\033[m")


        item_a_ser_removido = itens[item_a_ser_removido - 1]



        carrinho1.remover_item(item_a_ser_removido)



#carrinho1.atualizar_quantidade_de_um_item("batata", 2000)


    elif escolha_usuario == 3:

        carrinho1.ver_carrinho_de_compra()

    
    elif escolha_usuario == 4:


        itens = list(carrinho1.itens_do_carrinho.keys())

        quantidade_itens = list(carrinho1.itens_do_carrinho.values())


        for posicao, item in enumerate(itens):

            qtd_item = quantidade_itens[posicao]

            print(f"{posicao + 1} - {item} (qtd: {qtd_item})")


        while True:


            item_a_ser_atualizado = int(input("Item a ser atualizado: "))


            if item_a_ser_atualizado in range(1, len(itens) + 1):

                break

            print("\033[1;31mItem inexistente. Por favor, tente novamente.\033[m")

    
        nova_quantidade_do_item_a_ser_atualizado = int(input("Nova quantidade: "))


        item_a_ser_atualizado = itens[item_a_ser_atualizado - 1]

        carrinho1.itens_do_carrinho[item_a_ser_atualizado] = nova_quantidade_do_item_a_ser_atualizado




    elif escolha_usuario == 5:


        continuar = False