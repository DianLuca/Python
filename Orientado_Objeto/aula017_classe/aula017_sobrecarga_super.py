class ClassePai:  # Super Classe
    # Método Construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Método que vai ser sobrecarregado
    def metodo_classe(self):
        print('--- Método da Classe Pai ---')
        print('Aqui vou multiplicar a e b!')
        resultado = self.a + self.b
        print('Este cálculo está sendo realizado pelo Método da Classe Pai!')
        print(f'O resultado da soma de {self.a} e {self.b} = {resultado}')
        
class ClasseFilha(ClassePai): # Classe Derivada
    # Método Construtor
    def __init__(self, a, b):
        super().__init__(a, b) # Chama o contrutor da classe pai
        # Não é necessário redefinir a variável com self.a e self.b,
        # pois já foram inicializadas pelo construtor da classe pai
    
    # Sobrecarga de Método
    def metodo_classe(self):
        # Primeiro, executa o método da classe pai
        super().metodo_classe()
        # Depois, executa o método da classe filha
        resultado = self.a + self.b
        print('\n--- Método da Classe Filha ---')
        print(f'O resultado da soma na Classe Filha é: {resultado}')

# Programa principal
# teste = ClassePai(1, 2) # Executa apenas o método da classe pai
teste = ClasseFilha(1, 2) # Executa ambos os métodos pois o método do 'pai' 
# é chamado novamente na linha 24
teste.metodo_classe()