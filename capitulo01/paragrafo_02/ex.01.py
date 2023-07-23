class Carro:
    # MÃ©todo construtor para inicializar as caracterÃ­sticas do carro
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    # MÃ©todo para acelerar o carro
    def acelerar(self, incremento):
        self.velocidade += incremento

    # MÃ©todo para frear o carro
    def frear(self, decremento):
        self.velocidade -= decremento

    # MÃ©todo para exibir as informaÃ§Ãµes do carro
    def mostrar_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")


# Criando um objeto a partir da classe Carro
meu_carro = Carro(marca="Toyota", modelo="Corolla", ano=2021, cor="Prata")

# Acelerando o carro
meu_carro.acelerar(50)

# Exibindo as informaÃ§Ãµes do carro
meu_carro.mostrar_informacoes()
