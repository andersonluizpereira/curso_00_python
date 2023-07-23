# Classe base (superclasse)
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print("O veículo está acelerando.")

# Classe derivada (subclasse) - Carro
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)  # Chama o construtor da classe base
        self.num_portas = num_portas

    def acelerar(self):
        print("O carro está acelerando.")

    def abrir_porta(self):
        print("Abrindo a porta do carro.")

# Classe derivada (subclasse) - Bicicleta
class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, num_marchas):
        super().__init__(marca, modelo, ano)  # Chama o construtor da classe base
        self.num_marchas = num_marchas

    def acelerar(self):
        print("A bicicleta está acelerando.")

    def trocar_marcha(self):
        print("Trocar a marcha da bicicleta.")

# Criando objetos das classes derivadas
meu_carro = Carro(marca="Toyota", modelo="Corolla", ano=2021, num_portas=4)
minha_bicicleta = Bicicleta(marca="Caloi", modelo="Explorer", ano=2022, num_marchas=18)

# Chamando métodos das classes derivadas
meu_carro.acelerar()  # Saída: O carro está acelerando.
meu_carro.abrir_porta()  # Saída: Abrindo a porta do carro.

minha_bicicleta.acelerar()  # Saída: A bicicleta está acelerando.
minha_bicicleta.trocar_marcha()  # Saída: Trocar a marcha da bicicleta.

# Chamando método da classe base
meu_carro.acelerar()  # Saída: O veículo está acelerando.
