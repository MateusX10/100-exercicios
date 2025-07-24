from classes import *



nome = str(input("Nome: "))

idade = int(input("Idade: "))


pessoa1 = Pessoa(nome, idade)


assunto = str(input("Assunto: "))


pessoa1.falar(assunto=assunto)
