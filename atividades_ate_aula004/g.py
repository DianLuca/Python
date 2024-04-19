# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 19/04/2024
# Faça um programa que converta metros em centímetros e milímetros.

# Imports
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
metros = float(input('Insira um valor em metros: '))

# Processamento 
centimetros = metros * 100
milimetros = metros * 1000

# Saída
print('-' * 70)
print('--- RESULTADO')
print('=' * 70)
print(f'{metros} metros possuí em centímetros: {centimetros:.0f} cm e em '
      + f'milímetros: {milimetros:.0f} mm')