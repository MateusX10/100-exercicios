from funcs import *


usuarios = {}


opcoes_validas = [1, 2, 3, 4]


continuar = True

while continuar:


    menu()

    while True:
        escolha_usuario = int(input("Escolha uma opção: "))


        if escolha_usuario in opcoes_validas:


            
            break


    if escolha_usuario == 1:

        id_usuario = 1 if not usuarios else len(usuarios) + 1

        nome = str(input("Nome: "))

        idade = int(input("Idade: "))


        usuarios[id_usuario] = [nome, idade]


    elif escolha_usuario == 2:


        
        print(f"{'id':<3}{'nome':>5}{'idade':>20}")


        for chave, valor in usuarios.items():

            print(f"{str(chave):<3}{str(valor[0]):>5}{str(valor[1]):>20} anos")


        usuario_a_ser_removido = int(input("ID do usuário a ser removido: "))


        del usuarios[usuario_a_ser_removido]        

    elif escolha_usuario == 3:

        #print(usuarios)

        print(f"{'id':<3}{'nome':>5}{'idade':>20}")


        for chave, valor in usuarios.items():

            print(f"{str(chave):<3}{str(valor[0]):>5}{str(valor[1]):>20} anos")

    elif escolha_usuario == 4:

        continuar = False