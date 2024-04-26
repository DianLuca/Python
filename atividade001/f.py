# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 19/04/2024
# Faça um programa que receba um número qualquer e calcule o dobro e o triplo 
# desse número.

# Imports
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
valor = float(input('Insira qualquer valor: '))

# Processamento
dobro = valor * 2
triplo = valor * 3

# Saída
print('-' * 70)
print('--- RESULTADO')
print('=' * 70)
print(f'O dobro e o triplo do valor {valor} são respectivamente: '
      + f'{dobro} e {triplo}')
