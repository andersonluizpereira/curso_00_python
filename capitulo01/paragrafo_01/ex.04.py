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
# Função que aceita um objeto Animal e chama o método fazer_som()
def fazer_barulho(animal):
    animal.fazer_som()

# Criando objetos
animal_generico = Animal("Animal Genérico")
cachorro = Cachorro("Bolt")

fazer_barulho(animal_generico)  # Saída: Algum som genérico
fazer_barulho(cachorro)         # Saída: Au au!
