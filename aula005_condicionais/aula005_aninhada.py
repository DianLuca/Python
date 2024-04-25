# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca
# Data: 25/04/2024
# Práticas com condicionais simples e aninhadas

import os


os.system('cls')

# Declarações
a = input('Insira um valor: ')
b = input('Insira um valor: ')
resposta = ''

print('-' * 70)
print('Estudo de Condicionais (Simples)')
print('=' * 70)

# Condicionais
if a > b:
    resposta = f'{a} é maior que {b}'
else:
    resposta = f'{a} não é maior que {b}'
    
# Saída
print()
print(resposta)
print('-' * 70)
print()

# Novas declarações
a1 = input('Insira outro valor...: ')
b1 = input('Insira um outro valor: ')

print('-' * 70)
print('Estudo de condicionais (Aninhada)')
print('=' * 70)

if a1 > b1:
    resposta = f'{a1} é maior que {b1}'
elif a1 < b1:
    resposta = f'{a1} é menor que {b1}'
else:
    resposta = f'Os valores são iguais: {a1} = {b1}'

# Saída
print('-' * 70)
print(resposta)
print('-' * 70)
print()