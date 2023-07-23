class Numero:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, outro_numero):
        return Numero(self.valor + outro_numero.valor)

num1 = Numero(5)
num2 = Numero(10)
resultado = num1 + num2
print(resultado.valor)  # Saida: 15
