class ContaBancaria:

    def __init__(self, titular, numero, agencia, saldo, tipo_conta):


        self.titular = titular

        self.numero = numero

        self.agencia = agencia

        self.saldo = saldo
        
        self.tipo_conta = tipo_conta



    
    def mostrar_informacoes_da_conta(self):

        print(f'''Informações da conta de {self.titular}:
- titular: {self.titular};
- Número: {self.numero};
- Agência: {self.agencia};
- Saldo: R${self.saldo:.2f};
- Tipo da conta: {self.tipo_conta}.
              ''')


        


    def sacar(self, valor):


        if self.saldo >= valor:

            self.saldo -= valor


        valor_sacado = valor


        return valor_sacado
    


    def depositar(self, valor):


        self.saldo += valor
            