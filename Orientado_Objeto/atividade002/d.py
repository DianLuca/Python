# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que imprima os números pares entre 0 e 100.
import os


class Numeros:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim


class Pares(Numeros):
    def par(self):
        c_par = 0
        for c in range(self.inicio, (self.fim + 1)):
            if (c % 2 == 0):
                c_par += 1
                print(c, end=' | ')
        return c_par


os.system('cls')

print('MOSTRADOR DE NÚMEROS PARES')
print()
print('INSIRA O INTERVALO DESEJADO:')
inicio = int(input('Insira o menor número: '))
fim = int(input('Insira o maior número: '))
print()
print(f'Os números pares no intervalo entre {inicio} e {fim}, serão: ')
numeros = Pares(inicio, fim)
c_par = numeros.par()
print(f'\nOs existe {c_par} número(s) par(es) nesse intervalo.')
