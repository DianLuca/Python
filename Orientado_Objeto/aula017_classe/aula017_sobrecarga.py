# Sobrecarga de Métodos

class ClassePai:  # Super Classe
    # Método Construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Para sobrecarregar
    # Vai ser usada para soma 2 números
    def metodo_classe(self, a, b):
        pass


# Herança
class ClasseFilha(ClassePai):  # Classe Derivada
    # Método construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Sobrecarga de Método
    def metodo_classe(self):
        return self.a + self.b


# Programa principalmente
teste = ClasseFilha(1, 2)
resultado = teste.metodo_classe()
# Apenas para exibir o resultado retornado
print(resultado)
