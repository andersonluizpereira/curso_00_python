class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

    def fazer_aniversario(self):
        self.idade += 1

# Criando um objeto a partir da classe Pessoa
pessoa1 = Pessoa("João", 30)

# Chamando o método 'apresentar' do objeto
pessoa1.apresentar()  # Saída: Olá, meu nome é João e tenho 30 anos.

# Chamando o método 'fazer_aniversario' do objeto
pessoa1.fazer_aniversario()

# Chamando novamente o método 'apresentar' para verificar a mudança de idade
pessoa1.apresentar()  # Saída: Olá, meu nome é João e tenho 31 anos.
