from abc import ABC, abstractmethod

# Classe abstrata
class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    # Método abstrato que deve ser implementado pelas subclasses
    @abstractmethod
    def emitir_som(self):
        pass

# Subclasses que herdam da classe abstrata Animal
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

# Tentar instanciar uma classe abstrata resultará em um erro
# animal = Animal("Bob")  # TypeError: Can't instantiate abstract class Animal with abstract methods emitir_som

# Criando objetos das subclasses
cachorro = Cachorro("Rex")
gato = Gato("Felix")

# Chamando o método emitir_som das subclasses
cachorro.emitir_som()  # Saída: Au au!
gato.emitir_som()      # Saída: Miau!
