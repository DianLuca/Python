# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 19/04/2024
# Faça um programa que receba um número inteiro, depois imprima sua 
# tabuada de multiplicação.

# Imports
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
numero_inteiro = int(input('Insira um número inteiro: '))

# Processamento
valor1 = numero_inteiro * 1
valor2 = numero_inteiro * 2
valor3 = numero_inteiro * 3
valor4 = numero_inteiro * 4
valor5 = numero_inteiro * 5
valor6 = numero_inteiro * 6
valor7 = numero_inteiro * 7
valor8 = numero_inteiro * 8
valor9 = numero_inteiro * 9
valor10 = numero_inteiro * 10

# Saída
print('-' * 70)
print(f'--- RESULTADO DA TABUADA DE {numero_inteiro}')
print('=' * 70)
print(f'{numero_inteiro} x 1 = {valor1} \n{numero_inteiro} x 2 = {valor2} \n'
      + f'{numero_inteiro} x 3 = {valor3} \n{numero_inteiro} x 4 = {valor4} \n'
      + f'{numero_inteiro} x 5 = {valor5} \n{numero_inteiro} x 6 = {valor6} \n'
      + f'{numero_inteiro} x 7 = {valor7} \n{numero_inteiro} x 8 = {valor8} \n'
      + f'{numero_inteiro} x 9 = {valor9} \n{numero_inteiro} x 10 = {valor10} \n')