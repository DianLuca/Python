# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Evolua o programa anterior para um código que pergunte ao usuário qual o
# intervalo que ele deseja ver  impresso.
import os


class Intervalo:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
    def exibir(self, inicio, fim):
        print()
        


class Apresentar(Intervalo):
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def exibir(self):
        for c in range(self.inicio, (self.fim + 1)):
            print(c, end=' - ')


os.system('cls')

print('QUAL O INTERVALO DESEJADO')
a = int(input('Insira o valor inicial: '))
b = int(input('Insira o valor fim....: '))
apresentar = Apresentar(a, b)
exibir = apresentar.exibir()
