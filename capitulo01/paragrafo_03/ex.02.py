#Exemplo de uma classe com métodos:

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

# Criando um objeto a partir da classe ContaBancaria
conta1 = ContaBancaria("João", 1000)

# Usando os métodos do objeto
conta1.depositar(500)
print(conta1.saldo)  # Saída: 1500

sucesso_saque = conta1.sacar(2000)
print(sucesso_saque)  # Saída: False (não há saldo suficiente para o saque)

sucesso_saque = conta1.sacar(1000)
print(sucesso_saque)  # Saída: True (saque realizado com sucesso)
print(conta1.saldo)   # Saída: 500
