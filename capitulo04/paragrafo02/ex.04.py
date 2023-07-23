class Professor:
    def __init__(self, nome):
        self.nome = nome

class Disciplina:
    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self, codigo, professor, disciplinas):
        self.codigo = codigo
        self.professor = professor
        self.disciplinas = disciplinas

# Criando objetos e estabelecendo a associação com multiplicidade
professor1 = Professor("Carlos")
disciplina1 = Disciplina("Matemática")
disciplina2 = Disciplina("História")

turma1 = Turma(codigo="T01", professor=professor1, disciplinas=[disciplina1, disciplina2])

print(f"Código da Turma: {turma1.codigo}")
print(f"Professor da Turma: {turma1.professor.nome}")
print("Disciplinas da Turma:")
for disciplina in turma1.disciplinas:
    print(f"- {disciplina.nome}")
