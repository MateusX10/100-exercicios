alunos = []

aluno = []

soma = quantidade = media = maior_nota = 0

aluno_que_tirou_maior_nota = ''


continuar = True

while continuar:

    aluno = (str(input("Nome do aluno: ")),
             float(input("Média do aluno: ")))
    

    alunos.append(aluno)


    while True:


        continuar_ou_nao = str(input("Continuar[S/N]?")).strip().upper()[0]


        if continuar_ou_nao in "SsNn":

            if continuar_ou_nao in "Nn":

                continuar = False

            break

        print("\033[1;31mOpção inválida. Por favor, tente novamente.\033[m")



quantidade = len(alunos)

for aluno in alunos:

    soma += aluno[1]

media = soma / quantidade 


print(f"Média geral da turma: {media:.2f}")



for aluno in alunos:


    if aluno[1] > maior_nota:

        maior_nota = aluno[1]

        aluno_que_tirou_maior_nota = aluno[0]



print(f'''O aluno que tirou a maior nota foi {aluno_que_tirou_maior_nota}.
Sua nota foi: {maior_nota:.2f}''')