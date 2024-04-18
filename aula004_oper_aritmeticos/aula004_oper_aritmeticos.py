# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca
# Data: 17/04/2024
# Operadorses Aritméticos

# imports
import os

# limpar o terminal
os.system('cls')

print('-' * 70)
print('OPERADORES ARITMÉTICOS')
print('-' * 70)

# Entrada de dados
print('--- SOMA')
print('-' * 70)
parcela_1 = float(input('Entre com a 1ª parcela: '))
parcela_2 = float(input('Entre com a 2ª parcela: '))

print()
print('--- SUBSTRAÇÃO')
print('-' * 70)
minuendo = float(input('Entre com o minuendo: '))
subtraendo = float(input('Entre com o subtraendo: '))

print()
print('--- PRODUTO')
print('-' * 70)
multiplicando = float(input('Entre com o multiplicando: '))
multiplicador = float(input('Entre com o multiplicador: '))

print()
print('--- DIVISÃO')
print('-' * 70)
dividendo = float(input('Entre com o dividendo: '))
divisor = float(input('Entre com o divisor: '))

print()
print('--- Raizes')
print('-' * 70)
radicando = float(input('Insira um valor para calcular a raiz quadrada: '))
indice = float(input('Insira o índice da raiz: ')) 

# Processamento
soma = parcela_1 + parcela_2
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor
raiz_quadrada = radicando ** (1/2)
raiz_cubica = radicando ** (1/3) 
raiz_indice = radicando ** (1/indice)

# Saída
print('=' * 70)
print('RESULTADOS')
print('-' * 70)
print(f'A soma de {parcela_1} + {parcela_2} é: {soma}')
print(f'A subtração de {minuendo} - {subtraendo} é: {diferenca}')
print(f'A multiplicação de {multiplicando} x {multiplicador} é: {produto}')
print(f'A divisão de {dividendo} / {divisor} é: {quociente}')

# Saída das raizes
print(f'A raiz quadrada do valor {radicando} é: {raiz_quadrada}')
print(f'A raiz cúbica do valor {radicando} é: {raiz_cubica}')
print(f'A raiz de indice: {indice} e de radicando: {radicando} é: {raiz_indice}')

# FIM