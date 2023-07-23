Vamos criar um exemplo que aborde todas essas características da programação orientada a objetos em Python. Neste exemplo, criaremos um sistema de transporte que envolve diferentes tipos de veículos, como carros e bicicletas. Vamos utilizar classes, getters e setters, encapsulamento, herança, abstração, polimorfismo e composição para modelar esse sistema.

**1. Classe Veiculo (Classe Base):**
```python
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    def get_marca(self):
        return self._marca

    def set_marca(self, nova_marca):
        self._marca = nova_marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, novo_modelo):
        self._modelo = novo_modelo

    def get_ano(self):
        return self._ano

    def set_ano(self, novo_ano):
        self._ano = novo_ano

    def exibir_info(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Ano: {self._ano}"
```

**2. Classe Carro (Classe Derivada):**
```python
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self._num_portas = num_portas

    def get_num_portas(self):
        return self._num_portas

    def set_num_portas(self, novo_num_portas):
        self._num_portas = novo_num_portas

    def exibir_info(self):
        info_carro = super().exibir_info()
        return f"{info_carro}, Número de Portas: {self._num_portas}"
```

**3. Classe Bicicleta (Classe Derivada):**
```python
class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, num_marchas):
        super().__init__(marca, modelo, ano)
        self._num_marchas = num_marchas

    def get_num_marchas(self):
        return self._num_marchas

    def set_num_marchas(self, novo_num_marchas):
        self._num_marchas = novo_num_marchas

    def exibir_info(self):
        info_bicicleta = super().exibir_info()
        return f"{info_bicicleta}, Número de Marchas: {self._num_marchas}"
```

**4. Composição - Classe Pessoa:**
```python
class Pessoa:
    def __init__(self, nome, veiculo):
        self._nome = nome
        self._veiculo = veiculo

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def exibir_info(self):
        return f"Nome: {self._nome}, Veículo: {self._veiculo.exibir_info()}"
```

**Testando o Código:**
```python
# Criando objetos de Carro e Bicicleta
carro1 = Carro("Toyota", "Corolla", 2022, 4)
bicicleta1 = Bicicleta("Caloi", "Elite", 2021, 21)

# Testando herança e polimorfismo
print(carro1.exibir_info())
# Saída: Marca: Toyota, Modelo: Corolla, Ano: 2022, Número de Portas: 4

print(bicicleta1.exibir_info())
# Saída: Marca: Caloi, Modelo: Elite, Ano: 2021, Número de Marchas: 21

# Criando objeto de Pessoa com composição
pessoa1 = Pessoa("João", carro1)
pessoa2 = Pessoa("Maria", bicicleta1)

# Testando encapsulamento e composição
print(pessoa1.exibir_info())
# Saída: Nome: João, Veículo: Marca: Toyota, Modelo: Corolla, Ano: 2022, Número de Portas: 4

print(pessoa2.exibir_info())
# Saída: Nome: Maria, Veículo: Marca: Caloi, Modelo: Elite, Ano: 2021, Número de Marchas: 21

# Testando getters e setters
pessoa1.set_nome("Pedro")
print(pessoa1.get_nome())  # Saída: Pedro

carro1.set_num_portas(2)
print(carro1.get_num_portas())  # Saída: 2

bicicleta1.set_num_marchas(18)
print(bicicleta1.get_num_marchas())  # Saída: 18
```

Neste exemplo, utilizamos todas as características mencionadas (classes, getters e setters, encapsulamento, herança, abstração, polimorfismo e composição) para modelar um sistema simples de transporte com carros e bicicletas. Cada classe representa um objeto com seus respectivos atributos e métodos, e a composição é utilizada para relacionar uma classe Pessoa com a classe Veiculo, permitindo que uma pessoa possua um veículo específico. Os getters

 e setters garantem o acesso controlado aos atributos privados, e o polimorfismo é demonstrado ao chamar o método `exibir_info()` em objetos de diferentes classes, produzindo saídas específicas para cada tipo de veículo.