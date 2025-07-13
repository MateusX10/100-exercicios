notas = ["100", "50", "20", "10", "5", "2", "1"]

valores_notas = {"100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0}



dinheiro_de_entrada = float(input("Digite o valor em dinheiro: R$"))

for nota in notas:

    if dinheiro_de_entrada >= int(nota):

        while dinheiro_de_entrada >= int(nota):

            valores_notas[nota] += 1

            dinheiro_de_entrada -= int(nota)


print(f"Serão necessárias: \n")

for nota, valor in valores_notas.items():

    print(f"- {valor} notas de  R${nota},00" if valor > 0 else "")


        