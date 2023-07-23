class ContaBancaria:
    def __init__(self, numero_conta, saldo):
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

class Cliente:
    def __init__(self, nome, cpf, conta):
        self.nome = nome
        self.cpf = cpf
        self.conta = conta

    def exibir_saldo(self):
        print(f"Saldo do cliente {self.nome}: R${self.conta.saldo:.2f}")

# Criando objetos e relacionando-os por composição
conta_cliente1 = ContaBancaria(numero_conta="1234", saldo=1000)
cliente1 = Cliente(nome="João", cpf="111.111.111-11", conta=conta_cliente1)

cliente1.exibir_saldo()  # Saída: Saldo do cliente João: R$1000.00

cliente1.conta.depositar(500)
cliente1.exibir_saldo()  # Saída: Saldo do cliente João: R$1500.00

cliente1.conta.sacar(2000)  # Saída: Saldo insuficiente.
