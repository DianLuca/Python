# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 19/04/2024
# Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.

# import
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota.: '))
nota3 = float(input('Insira a terceira nota: '))
nota4 = float(input('Insira a quarta nota..: '))

# Processamento
soma = nota1 + nota2 + nota3 + nota4
media = soma / 4

# Saída
print('-' * 70)
print('--- RESULTADO')
print(f'A média das nota 1: {nota1} | nota 2: {nota2} |'
      + f'nota 3: {nota3} | nota 4: {nota4} é: {media}')
