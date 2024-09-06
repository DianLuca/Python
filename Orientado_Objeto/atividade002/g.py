# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que calcule os números primos em um intervalo
# pré-determinado pelo usuário.
import os


os.system('cls')

print('NÚMEROS PRIMOS')
print()

a = int(input('Insira um número para começar..: '))
b = int(input('Insira um número para finalizar: '))

if a < 2: 
    print(f'Não existe número primo de {a}, portando adotaremos o menor mais ' 
          + f'próximo: 2')
    a = 2

for c in range(a, (b + 1)):
    for i in range(a, c):
        if c % i == 0:
            break
    else:
        print(c, end=' | ')
