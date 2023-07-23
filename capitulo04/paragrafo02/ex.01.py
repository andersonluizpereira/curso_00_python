class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"{self.marca} {self.modelo}"

class Pessoa:
    def __init__(self, nome, carro):
        self.nome = nome
        self.carro = carro  # Associação simples com a classe Carro

    def dirigir_carro(self):
        print(f"{self.nome} está dirigindo o carro {self.carro.exibir_info()}.")

# Criando objetos e estabelecendo a associação simples
carro1 = Carro("Toyota", "Corolla")
pessoa1 = Pessoa("João", carro1)

pessoa1.dirigir_carro()  # Saída: João está dirigindo o carro Toyota Corolla.
