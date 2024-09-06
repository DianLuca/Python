# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que imprima os números no intervalo entre 1 e 100.
# Os números devem ser apresentados na horizontal.
import os


class Intervalo:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim


class Apresentar(Intervalo):

    def exibir(self):
        for c in range(self.inicio, self.fim):
            print(c, end=' - ')


os.system('cls')

intervalo = Apresentar(1, 101)
exibir = intervalo.exibir()
