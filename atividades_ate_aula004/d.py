# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 19/04/2024
# Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.

# imports
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
valor1 = float(input('Insira o primeiro valor: '))
valor2 = float(input('Insira o segundo valor.: '))

# Processamento
divisao = valor1 / valor2

# Saída
print()
print('--- RESULTADO')
print(f'O resultado da divisão será: {divisao:.4f}')
