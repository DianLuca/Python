# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca
# Data: 24/04/2024
# Operadores Lógicos

import os


os.system('cls')

print('-' * 70)
print('Estudo de Condicional: Parte 1')
print('=' * 70)

# Entrada
valor = float(input('Digite um número: '))
resposta = ''

# Condicional
if valor % 2 == 0:
    resposta = f'Entrada incorreta, o valor {valor} é par!'
else:
    resposta = f'Entrada correta, o valor {valor} é um ímpar!'

# Saída
print('=' * 70)
print(resposta)

print('Fim do programa! \n') # \n salta uma linha