class Pessoa:
    def __init__(self, nome):
        self.__nome = nome  # Atributo protegido com dois underscores

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

pessoa = Pessoa("Bob")
print(pessoa.get_nome())  # Saída: Bob

# Tentar acessar diretamente um atributo protegido resultará em um nome transformado
print(pessoa.__nome)  # Saída: AttributeError: 'Pessoa' object has no attribute '__nome'
#print(pessoa._Pessoa__nome)  # Saída: Bob (Acessando o atributo protegido com o nome transformado)
