# Classe base (superclasse)
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("Algum som genérico")

# Classe derivada (subclasse)
class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

# Criando objetos
animal_generico = Animal("Animal GenÃ©rico")
cachorro = Cachorro("Bolt")

animal_generico.fazer_som()  # Saída: Algum som genérico
cachorro.fazer_som()         # Saída: Au au!
