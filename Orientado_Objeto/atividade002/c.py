# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que imprima os números no intervalo entre 1 e 10
# em ordem inversa.
import os


os.system('cls')

print('PARA CONTAGEM REGRESSIVA')
print()

a = int(input('Insira o maior número: '))
b = int(input('Insira o menor número: '))
print()
c = 0

for c in range(a, (b - 1), -1):
    print(c, end=' | ')