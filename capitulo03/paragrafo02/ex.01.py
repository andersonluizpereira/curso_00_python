# Exemplo de abstração usando uma classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print(f"{self.marca} {self.modelo} está acelerando.")

# Criando objetos usando a classe Carro
carro1 = Carro(marca="Toyota", modelo="Corolla", ano=2021)
carro2 = Carro(marca="Honda", modelo="Civic", ano=2022)

# Chamando o método acelerar para os objetos
carro1.acelerar()  # Saída: Toyota Corolla está acelerando.
carro2.acelerar()  # Saída: Honda Civic está acelerando.
