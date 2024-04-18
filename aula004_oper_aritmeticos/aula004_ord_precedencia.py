# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca
# Data: 18/04/2024
# Operadores Aritméticos: Ordem de Precedência

import os


os.system('cls')

print('-' * 70)
print('Operadores Aritméticos: Ordem de Precedência')
print('-' * 70)

nota1 = float(input('insira a primeira nota: '))
nota2 = float(input('insira a segunda nota: '))
nota3 = float(input('insira a terceira nota: '))
nota4 = float(input('insira a quarta nota: '))

soma = nota1 + nota2 + nota3 + nota4
media = nota1 + nota2 + nota3 + nota4 / 4
media_correta = (nota1 + nota2 + nota3 + nota4) / 4

print('-' * 5 + 'NOTAS' + '-' * 5)
print(f'Nota 1: {nota1}, Nota 2: {nota2} | '
      + f'Nota 3: {nota3} e Nota 4: {nota4}')
print('-' * 70)
print(f'Média errada: {media}')
print(f'Média correta: {media_correta}')
print('-' * 70)