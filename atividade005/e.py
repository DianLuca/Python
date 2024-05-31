# Faça um programa que some a quantidade de números pares encontrados 
# no intervalo entre 0 e 100.
import os 


os.system('cls')

print('SOMATÓRIO DE NÚMEROS PARES')
print()

a = int(input('Insira o menor número: '))
b = int(input('Insira o maior número: '))
print()

c = 0
soma = 0

for c in range(a, (b + 1), 2):
    numero = c
    
    soma += numero
    
    print(soma, end=' | ')