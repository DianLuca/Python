# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 19/04/2024
# Faça um programa que receba um número inteiro e mostre o sucessor 
# e antecessor.

# imports
import os


os.system('cls')


print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
valor = int(input('Insira um valor:'))

# Processamento
antecessor = valor - 1
sucessor = valor + 1

# Saída
print('-' * 70)
print('--- RESULTADO')
print('=' * 70)
print(f'O antessessor e o sucessor do valor: {valor}, são os seguintes ' 
      + f'respectivamentes: {antecessor} e {sucessor}')