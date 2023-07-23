# Definição da classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando objetos a partir da classe Pessoa
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

# Chamando o método apresentar() em cada objeto
pessoa1.apresentar()  # Saída: Olá, meu nome é João e tenho 30 anos.
pessoa2.apresentar()  # Saída: Olá, meu nome é Maria e tenho 25 anos.
