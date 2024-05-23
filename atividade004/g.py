# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 23/05/2024
# G) Faça um programa que receba um número inteiro e mostre na tela:
# • A quantidade de unidades, a quantidade de dezenas, a quantidade 
# de centenas e a quantidade de milhares.

import os


os.system('cls')

numero = int(input('Insira um número inteiro: '))

unidades = numero % 10
dezenas = (numero // 10) % 10
centenas = (numero // 100) % 10
milhares = (numero // 1000) % 10

print(f'O número: "{numero}" possui {unidades} unidade(s), {dezenas} '
      + f'dezena(s), {centenas} centena(s) e {milhares} milhar(es)')