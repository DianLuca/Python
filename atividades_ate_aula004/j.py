# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 19/04/2024
# Faça um programa com entrada de dados para calcular o perímetro de um retângulo.

# Imports
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
print('-- Calculando o perímetro de um retângulo --')
base = float(input('Insira a base do retângulo (em cm): '))
altura = float(input('Insira a altura do retângulo (em cm): '))

# Processamento
perimetro_retangulo = 2*(base + altura)

# Saída
print('-' * 70)
print('-- RESULTADO')
print('=' * 70)
print(f'O perímetro de um retângulo de base: {base:.2f} cm e altura: '
      + f'{altura:.2f} cm é de: {perimetro_retangulo:.2f} cm')
