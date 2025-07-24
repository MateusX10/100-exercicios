from classes import ContaBancaria


titular = str(input("Titular da conta: "))

numero = str(input("Número da conta: "))


agencia = str(input("Número da agência bancária: "))

saldo = float(input("Saldo da conta: R$"))


while True:

    tipo_conta = str(input("Tipo da conta: "))  


    if tipo_conta in ["corrente", "poupança"]:

        break

    print("\033[1;31mOpção inválida. Por favor, digite somente 'corrente' ou 'poupança'.\033[m")


conta_bancaria1 = ContaBancaria(titular, numero, agencia, saldo, tipo_conta)


conta_bancaria1.mostrar_informacoes_da_conta()


conta_bancaria1.sacar(100)


conta_bancaria1.mostrar_informacoes_da_conta()


conta_bancaria1.depositar(1000)


conta_bancaria1.mostrar_informacoes_da_conta()