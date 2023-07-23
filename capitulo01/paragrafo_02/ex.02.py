class Carro:
    # Método construtor para inicializar as características do carro
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    # Método para acelerar o carro
    def acelerar(self, incremento):
        self.velocidade += incremento

    # Método para frear o carro
    def frear(self, decremento):
        self.velocidade -= decremento

    # Método para exibir as informações do carro
    def mostrar_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")


# Instanciando objetos a partir da classe Carro
carro1 = Carro(marca="Toyota", modelo="Corolla", ano=2021, cor="Prata")
carro2 = Carro(marca="Honda", modelo="Civic", ano=2022, cor="Preto")

# Acelerando e freando os carros
carro1.acelerar(50)
carro2.acelerar(30)
carro2.frear(10)

# Exibindo as informações dos carros
carro1.mostrar_informacoes()
carro2.mostrar_informacoes()

