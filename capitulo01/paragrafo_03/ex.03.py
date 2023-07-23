class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando um objeto a partir da classe Pessoa
pessoa1 = Pessoa("João", 30)

# Acessando os atributos do objeto
print(pessoa1.nome)  # Saída: João
print(pessoa1.idade)  # Saída: 30

# Modificando o valor do atributo 'idade'
pessoa1.idade = 35

# Acessando o novo valor do atributo 'idade'
print(pessoa1.idade)  # Saída: 35
