class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando um objeto a partir da classe Pessoa
pessoa1 = Pessoa("JoÃ£o", 30)

# Acessando os atributos do objeto
print(pessoa1.nome)  # SaÃ­da: JoÃ£o
print(pessoa1.idade) # SaÃ­da: 30
