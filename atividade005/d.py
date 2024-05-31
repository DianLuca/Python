# Faça um programa que imprima os números pares entre 0 e 100.
import os


os.system('cls')

print('MOSTRADOR DE NÚMEROS PARES')
print()
print('INSIRA O INTERVALO DESEJADO:')
a = int(input('Insira o menor número: '))
b = int(input('Insira o maior número: '))
print()

c = 0

print(f'Os números pares no intervalo entre {a} e {b}, serão: ')

for c in range(a, b + 1, 2):
    print(c, end=' | ')
