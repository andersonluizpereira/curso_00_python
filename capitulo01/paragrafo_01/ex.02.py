class Exemplo:
    def __init__(self):
        self.publico = "Atributo Público"
        self._privado = "Atributo Privado"
        self.__protegido = "Atributo Protegido"

obj = Exemplo()
print(obj.publico)      # Saída: Atributo Público
print(obj._privado)     # Saída: Atributo Privado
print(obj.__protegido)  # Erro: AttributeError: 'Exemplo' object has no attribute '__protegido'
