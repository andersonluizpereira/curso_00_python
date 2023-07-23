Vamos criar um exemplo em Python que abrange todas as características mencionadas: classes, getters e setters, objetos, encapsulamento, herança, abstração, polimorfismo e composição. Neste exemplo, vamos criar um sistema simples para uma loja de eletrônicos, com as classes `Produto`, `Eletronico`, `Smartphone`, e `CarrinhoDeCompras`. 

1. Classes e Encapsulamento:
Vamos criar a classe base `Produto`, que encapsula as informações básicas de um produto.

```python
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        self.__preco = preco
```

2. Herança e Polimorfismo:
Vamos criar a classe `Eletronico`, que herda de `Produto` e representa produtos eletrônicos em geral. Também vamos criar a classe `Smartphone`, que herda de `Eletronico` e representa smartphones específicos.

```python
class Eletronico(Produto):
    def __init__(self, nome, preco, marca):
        super().__init__(nome, preco)
        self.__marca = marca

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

class Smartphone(Eletronico):
    def __init__(self, nome, preco, marca, sistema_operacional):
        super().__init__(nome, preco, marca)
        self.__sistema_operacional = sistema_operacional

    def get_sistema_operacional(self):
        return self.__sistema_operacional

    def set_sistema_operacional(self, sistema_operacional):
        self.__sistema_operacional = sistema_operacional
```

3. Abstração:
Vamos criar a classe `CarrinhoDeCompras`, que abstrai o conceito de um carrinho de compras, onde podemos adicionar e listar produtos.

```python
class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []

    def adicionar_produto(self, produto):
        self.__produtos.append(produto)

    def listar_produtos(self):
        for produto in self.__produtos:
            print(f"{produto.get_nome()} - R${produto.get_preco():.2f}")
```

4. Composição:
O carrinho de compras pode conter vários produtos (eletrônicos ou não), portanto, usamos composição para relacionar o carrinho com os produtos.

Aqui está um exemplo de utilização das classes:

```python
# Criando objetos
produto1 = Produto("Mouse", 50.0)
smartphone1 = Smartphone("iPhone 13", 5000.0, "Apple", "iOS")

# Atribuindo valores usando setters
produto1.set_nome("Teclado")
produto1.set_preco(100.0)

# Acessando valores usando getters
print(produto1.get_nome())  # Saída: Teclado
print(produto1.get_preco())  # Saída: 100.0

# Criando carrinho de compras
carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(smartphone1)

# Listando produtos do carrinho
carrinho.listar_produtos()
# Saída:
# Teclado - R$100.00
# iPhone 13 - R$5000.00
```

Neste exemplo, usamos classes, getters, setters, encapsulamento, herança, abstração, polimorfismo e composição para criar um sistema simples de loja de eletrônicos. Cada classe tem sua responsabilidade bem definida, e a composição é usada para relacionar os produtos com o carrinho de compras. O polimorfismo é demonstrado pelo fato de que podemos adicionar diferentes tipos de produtos (eletrônicos ou não) ao carrinho.