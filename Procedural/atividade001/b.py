# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 19/04/2024
# Faça um programa que peça o ano do seu nascimento e calcule a sua idade.

# imports
import os
import datetime


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
print('-')
nascimento = int(input('Insira seu ano de nascimento: '))

# Processamento
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

# Saída
print('-' * 70)
print('--- RESULTADO')
print(f'Você possui {idade} anos.')
