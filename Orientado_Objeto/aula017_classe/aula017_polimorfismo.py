from math import pi

# Define a classe base Forma com um método área
# que não faz nada (quase uma classe abstrata)


class Forma:
    def area(self):
        pass

# Define a classe Circulo que herda de Forma
# O construtor __init__ inicializa o atributo raio


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    # Define o método area para calcular a área do
    # círculo usando a fórmula pi * raio²
    def area(self):
        return pi * (self.raio ** 2)

# Define a classe Retangulo que herda da Forma


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largula = largura
        self.altura = altura

    # Define o método área para calcular a área
    # do retângulo usando a fórmula largura * altura
    def area(self):
        return self.largula * self.altura

# Define a classe Quadrado que herda de Retangulo


class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

# Define uma função exibir_area que aceita um
# objeto forma e imprime sua área
# O método área é chamado no objeto forma


def exibir_area(forma):
    print(f'A área da forma é: {forma.area()}')


# Cria instâncias e Circulo, Retangulo e Quadrado
circulo = Circulo(5)
retangulo = Retangulo(4, 6)
quadrado = Quadrado(3)

# Chama a função exibir_area para cada instância
# O método área apropriado é chamado para
# cada objeto, mostrando polimorfismo

exibir_area(circulo)
exibir_area(retangulo)
exibir_area(quadrado)
