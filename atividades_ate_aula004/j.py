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
perimetro = 2*(base + altura)

# Saída
print('-' * 70)
print('-- RESULTADO')
print('=' * 70)
print(f'O perímetro de um retangulo de base: {base}cm e altura: {altura}cm '
      + f'é de: {perimetro}cm')
