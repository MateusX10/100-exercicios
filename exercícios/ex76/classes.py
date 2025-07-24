
class Pessoa:


    def __init__(self, nome, idade):

        self.nome = nome

        self.idade = idade


    def falar(self, assunto):

        print(f"{self.nome} está falando sobre {assunto}")

    