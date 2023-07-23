import math

# Classe base (superclasse)
class Shape:
    def area(self):
        pass

# Classe derivada (subclasse) - Círculo
class Circle(Shape):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

# Classe derivada (subclasse) - Retângulo
class Rectangle(Shape):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

# Função para calcular a área de qualquer figura
def calcular_area(figura):
    return figura.area()

# Criando objetos das classes derivadas
circulo = Circle(raio=5)
retangulo = Rectangle(base=4, altura=6)

# Calculando a área usando polimorfismo
area_circulo = calcular_area(circulo)
area_retangulo = calcular_area(retangulo)

print("Área do Círculo:", area_circulo)     # Saída: Área do Círculo: 78.53981633974483
print("Área do Retângulo:", area_retangulo) # Saída: Área do Retângulo: 24
