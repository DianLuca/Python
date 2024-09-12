# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que imprima os números no intervalo entre 1 e 10
# em ordem inversa.
import os


class Intervalo:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim


class Apresentar(Intervalo):
    def exibir(self):
        for c in range(self.fim, (self.inicio - 1), -1):
            print(c, end=' | ')


os.system('cls')

print('PARA CONTAGEM REGRESSIVA')
print()

a = int(input('Insira o menor número: '))
b = int(input('Insira o maior número: '))
apresentar = Apresentar(a, b)
apresentar.exibir()
