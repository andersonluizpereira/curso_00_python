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

class AgenciaBancaria:
    def __init__(self, numero_agencia):
        self.numero_agencia = numero_agencia
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        print(f"Contas da agência {self.numero_agencia}:")
        for conta in self.contas:
            print(f"- Conta: {conta.numero_conta}, Saldo: R${conta.saldo:.2f}")

# Criando objetos e relacionando-os por composição
conta1 = ContaBancaria(numero_conta="5678", saldo=2000)
conta2 = ContaBancaria(numero_conta="9012", saldo=3000)

agencia = AgenciaBancaria(numero_agencia="001")
agencia.adicionar_conta(conta1)
agencia.adicionar_conta(conta2)

agencia.listar_contas()
# Saída:
# Contas da agência 001:
# - Conta: 5678, Saldo: R$2000.00
# - Conta: 9012, Saldo: R$3000.00
