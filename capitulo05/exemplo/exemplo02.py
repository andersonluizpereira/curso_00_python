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

class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []

    def adicionar_produto(self, produto):
        self.__produtos.append(produto)

    def listar_produtos(self):
        for produto in self.__produtos:
            print(f"{produto.get_nome()} - R${produto.get_preco():.2f}")

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
