class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __del__(self):
        print(f"Objeto {self.nome} foi destruído.")
    def __str__(self):
        return f"{self.nome}, {self.idade} anos."

    def __repr__(self):
        return f"Pessoa('{self.nome}', {self.idade})"

pessoa1 = Pessoa("João", 30)

print(str(pessoa1))  # Saída: João, 30 anos.
print(repr(pessoa1))