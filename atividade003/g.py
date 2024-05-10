# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 10/05/2024
# G) Faça um programa que peça os valores de a, b e c de uma equação do
# 2º grau. Calcule as raízes da equação do 2º grau seguindo a
# fórmula: Δ = b² - 4ac, x = (-b ± raiz(Δ)) / (2a).

import math
import os


os.system('cls')

print('CALCULO DE EQUAÇÃO DO SEGUNDO GRAU')
print('-' * 70)

a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
c = float(input('Insira o valor de c: '))
print()

delta = b**2 - 4*a*c

if delta <= 0:
    print('Repita a operação, não se trata de uma equação de segundo grau pois' 
          + f'possui delta menor ou igual a 0')
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f'O resultado de x1 é: {x1} e de x2: {x2}')

print()
print('-' * 70)