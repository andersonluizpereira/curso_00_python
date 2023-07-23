class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []
        self.alunos = []

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

class Professor:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

class Aluno:
    def __init__(self, nome, serie):
        self.nome = nome
        self.serie = serie

# Criando objetos das classes
escola = Escola("Escola ABC")

professor1 = Professor("João", "Matemática")
professor2 = Professor("Maria", "História")

aluno1 = Aluno("Carlos", "8ª série")
aluno2 = Aluno("Ana", "9ª série")

# Relacionando os objetos por composição
escola.adicionar_professor(professor1)
escola.adicionar_professor(professor2)

escola.adicionar_aluno(aluno1)
escola.adicionar_aluno(aluno2)

# Imprimindo informações da escola, professores e alunos
print("Escola:", escola.nome)
print("Professores:")
for professor in escola.professores:
    print(f"- {professor.nome} ({professor.disciplina})")

print("Alunos:")
for aluno in escola.alunos:
    print(f"- {aluno.nome} ({aluno.serie})")
