class Carro:

    
    def __init__(self, marca, modelo, ano):

        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False



    
    def mostrar_informacoes_do_carro(self):

        print(f'''Informações do carro:
- Marca: {self.marca}

- Modelo: {self.modelo}

- Ano: {self.ano}
              ''')
        


    def ligar(self):


        if not self.ligado:

            self.ligado = True


            print("\033[1;32mO carro foi ligado!.\033[m")


        else:


            print("\033[1;31mO carro já está ligado.\033[m")



    def desligar(self):


        if self.ligado:
            
            self.ligado = False


            print("\033[1;32mO carro foi desligado.\033[m")


        else:

            
            print("\033[1;31mO carro já está desligado.\033[m")