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
