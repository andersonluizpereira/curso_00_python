class Animal:
    def emitir_som(self):
        print("Algum som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

def fazer_som(animal):
    animal.emitir_som()

cachorro = Cachorro()
gato = Gato()

fazer_som(cachorro)  # Saída: Au au!
fazer_som(gato)      # Saída: Miau!
