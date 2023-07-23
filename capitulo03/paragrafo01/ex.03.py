class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            print("Idade inválida.")

# Criando um objeto Pessoa
pessoa = Pessoa("Alice", 30)

# Usando os setters para modificar os valores dos atributos privados
pessoa.set_nome("Bob")
pessoa.set_idade(-5)  # Aviso de "Idade inválida."

# Usando os getters para obter os novos valores dos atributos privados
print(pessoa.get_nome())  # Saída: Bob
print(pessoa.get_idade()) # Saída: 30 (idade não foi modificada devido à validação no setter)
