# Exemplo de uma classe com atributos:

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando um objeto a partir da classe Pessoa
pessoa1 = Pessoa("João", 30)

# Acessando os atributos do objeto
print(pessoa1.nome)  # Saída: João
print(pessoa1.idade) # Saída: 30

