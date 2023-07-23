# Classe base (superclasse)
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        print("Algum som genérico")

# Classe derivada (subclasse)
class Cachorro(Animal):
    def __init__(self, nome, raca):
        # Chama o construtor da classe base
        super().__init__(nome, especie="Cachorro")
        self.raca = raca

    # Sobrescrevendo o método emitir_som da classe base
    def emitir_som(self):
        print("Au au!")

# Classe derivada (subclasse)
class Gato(Animal):
    def __init__(self, nome, cor):
        # Chama o construtor da classe base
        super().__init__(nome, especie="Gato")
        self.cor = cor

    # Sobrescrevendo o método emitir_som da classe base
    def emitir_som(self):
        print("Miau!")

# Criando objetos das classes derivadas
dog = Cachorro(nome="Rex", raca="Labrador")
cat = Gato(nome="Felix", cor="Preto")

# Chamando métodos das classes derivadas
dog.emitir_som()  # Saída: Au au!
cat.emitir_som()  # Saída: Miau!

# Chamando método da classe base
print(dog.nome)  # Saída: "Rex"
print(cat.especie)  # Saída: "Gato"
