# Faça um programa que imprima os números primos entre 0 e 100.
import os


os.system('cls')

print('NÚMEROS PRIMOS')
print()

a = int(input('Insira um número para começar: ')) # vide linha 14
b = int(input('Insira um número para finalizar:'))

for c in range(a, (b + 1)): # O número 0 e 1 não são primos
    for i in range(a, c): # O primeiro número primo é 2, então a >= 2
        if c % i == 0:
            break
    else:
        print(c)
