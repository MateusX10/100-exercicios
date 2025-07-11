class Carrinho_de_compra:


    def __init__(self):

        self.itens_do_carrinho = {}


    def adicionar_item(self, item, quantidade):


        self.itens_do_carrinho[item] = quantidade
        

    def remover_item(self, item):


        del self.itens_do_carrinho[item]


    
    def ver_carrinho_de_compra(self):


        for item, quantidade in self.itens_do_carrinho.items():


            print(f"- {item}: {quantidade}")



    def atualizar_quantidade_de_um_item(self, item,  nova_quantidade):


        if item in self.itens_do_carrinho.keys():

            self.itens_do_carrinho[item] = nova_quantidade

        else:

            print("\033[1;31mO item não existe!.\033[m")