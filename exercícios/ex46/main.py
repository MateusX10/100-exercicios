from funcs import *



inventario = {} # chave = item ; valor = quantidade do item


opcoes_validas_menu = [1, 2, 3, 4, 5, 6]


titulo_das_acoes_do_menu = ["Adicionar item", "Remover item", "Mostrar itens",
                            "Verificar se um item existe",
                            "Atualizar a quantidade de um item",
                            "Sair"]

continuar = True



while continuar:


    menu()


    while True:


        escolha_usuario = int(input("O que deseja fazer? "))


        if escolha_usuario in opcoes_validas_menu:

            break

        print("\033[1;31mOpção inválida. Por favor, tente novamente.\033[m")

    

    # mostra um título com a ação que o usuário escolhou no menu do inventário
    titulo(titulo_das_acoes_do_menu[escolha_usuario - 1])
    

    
    # Adicionar item
    if escolha_usuario == 1:


        item_a_ser_adicionado = str(input("Item: "))

        quantidade_do_item_a_ser_adicionado = int(input("Quantidade: "))


        inventario[item_a_ser_adicionado] = quantidade_do_item_a_ser_adicionado

    
    # Remover item
    elif escolha_usuario == 2:


        lista_do_inventario = list(inventario)


        opcoes_validas_da_lista_do_inventario = len(lista_do_inventario)


        for posicao, item in enumerate(lista_do_inventario):


            print(f"{posicao + 1} - {item}")


        while True:

            
            item_a_ser_removido = int(input("Qual item deseja remover? "))


            if 0 < item_a_ser_removido <= opcoes_validas_da_lista_do_inventario:


                break

            print("\033[1;31mO item não existe! Por favor, tente novamente.\033[m")

        

        item_a_ser_removido = lista_do_inventario[item_a_ser_removido - 1]


        del inventario[item_a_ser_removido]        


        #print(lista_do_inventario)


        

    
    # Mostrar itens
    elif escolha_usuario == 3:


        for item, quantidade_item in inventario.items():

            print(f"- {item}: {quantidade_item}")

    
    # Verificar se um item existe
    elif escolha_usuario == 4:



        item_a_ser_verificado = str(input("Item: "))


        if item_a_ser_verificado in inventario.keys():

            print(f'''\033[1;32mO item {item_a_ser_verificado} existe!\033[m''')
        
            print(f"Quantidade: {inventario[item_a_ser_verificado]}")


        else:


            print(f"\033[1;31mO item {item_a_ser_verificado} não existe!\033[m")

    
    # Atualizar quantidade de um item
    elif escolha_usuario == 5:



        lista_do_inventario = list(inventario)


        opcoes_validas_da_lista_do_inventario = len(lista_do_inventario)


        for posicao, item in enumerate(lista_do_inventario):


            print(f"{posicao + 1} - {item}")


        while True:

            
            item_a_ser_atualizado = int(input("Qual item deseja atualizar a quantidade? "))


            if 0 < item_a_ser_atualizado <= opcoes_validas_da_lista_do_inventario:


                break

            print("\033[1;31mO item não existe! Por favor, tente novamente.\033[m")
        

        item_a_ser_atualizado = lista_do_inventario[item_a_ser_atualizado - 1]

        nova_quantidade = int(input(f"Nova quantidade do item {item_a_ser_atualizado}: "))

        inventario[item_a_ser_atualizado] = nova_quantidade
        
    

    # Sair
    elif escolha_usuario == 6:


        continuar = False


    # ordena em ordem alfabética o dicionário de acordo
    # com os itens (chaves) a cada iteração
    inventario = dict(sorted(inventario.items()))