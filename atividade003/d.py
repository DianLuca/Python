# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 10/05/2024
# D) Faça um programa que receba um ângulo qualquer. Em seguida, calcule o
# seno, cosseno e tangente do ângulo, limitando a saída a 2 casas decimais.

import math
import os


os.system('cls')

print('CÁLCULO DE COSSENO, SENO E TANGENTE')
print('-' * 70)

angulo = float(input('Insira o valor de um ângulo: '))

cos = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f'O angulo de {angulo} possui: cosseno de: {cos:.2f}, seno de: {seno:.2f}, '
      + f'tangente de: {tan:.2f}')
