senha = "monk"


senha_valida = False

tentativas_efetuadas = 0


while not senha_valida and tentativas_efetuadas < 3:

    tentativa_usuario = str(input("Senha: "))

    if tentativa_usuario == senha:

        print("Acesso concedido")

        senha_valida = True

    else:

        print("Senha inválida. Tente novamente.")


    tentativas_efetuadas += 1