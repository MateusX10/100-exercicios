class Aluno:

    
    def __init__(self, nome, notas):


        self.nome = nome

        self.notas = notas

        self.media = 0

    def calcular_media(self):


        self.media = (self.notas[0] + self.notas[1]) / 2


        print(f"Média: {self.media:.2f}")