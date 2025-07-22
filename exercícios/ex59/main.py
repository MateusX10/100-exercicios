perguntas = {"1 - Qual é o maior planeta do Sistema Solar?": {"A": "Terra",
           "B": "Marte", "!C": "Júpiter", "D": "Saturno"},
           "2 - Quem escreveu a peça Romeu e Julieta?": {"!A": "William Shakespeare",
            "B": "Charles Dickens", "C": "Jane Austen", "D": "Machado de Assis"},
            "3 - Qual é a capital do Canadá?": {"A": "Toronto", "B": "Vancouver",
            "!C": "Ottawa", "D": "Montreal"},
            "4 - Em que ano o homem pisou na Lua pela primeira vez?": {"A": "1965",
            "!B": "1969", "C": "1972", "D": "1959"},
            "5 - Qual é o símbolo químico da água?": {"A": "CO2", "B": "O2",
            "!C": "H20", "D": "H2"}}


acertou_pergunta = False

resposta_certa = palpite_usuario =  ''

# exibe as perguntas
for pergunta, alternativa in perguntas.items():

    acertou_pergunta = False

    print(f"{pergunta} - ")

    for k, v in alternativa.items():

        print(f"{k.replace('!', '')} - {v}")


        # pega a alternativa correta
        if k[0] == "!":

            resposta_certa = f"{k} - {v}"


    # pergunta ao usuário qual a alternativa correta e valida se ele acertou ou não
    while not acertou_pergunta:

        palpite_usuario = str(input("\n-> Qual alternativa? ")).upper()[0]

        if palpite_usuario == resposta_certa[1]:

            print("\n\033[1;32m-> Acertou!\033[m")

            acertou_pergunta = True

        else:

            print("\n\033[1;31m-> Errou!\033[m")

    print("\n")


print("\033[1;32mVocê finalizou o quiz!\033[m")





