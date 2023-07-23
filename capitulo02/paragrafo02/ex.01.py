class Calculadora:
    def somar(self, a, b):
        return a + b

    def somar(self, a, b, c):
        return a + b + c

calc = Calculadora()
# print(calc.somar(2, 3))       # Saída: Erro! Método somar(a, b, c) está sobrescrevendo o anterior
print(calc.somar(2, 3, 4))    # Saída: 9 (a + b + c)
