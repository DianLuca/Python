# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que imprima os valores no intervalo definidos pelo usuário.
# Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos
# na tela.
import os


os.system('cls')

print('INSIRA UM INTERVALO E SELECIONE 3 NÚMEROS PARA IGNORAR')
print()
print('-- INTERVALO --')
inicial = int(input('Insira um número para iniciar.: '))
final = int(input('Insira um número para encerrar: '))
print('-- NÚMEROS IGNORADOS --')
primeiro = int(input('Insira o 1º número a ser ignorado: '))
segundo = int(input('Insira o 2º número a ser ignorado: '))
terceiro = int(input('Insira o 3º número a ser ignorado: '))

for c in range(inicial, (final + 1)):
    if ((c == primeiro) or (c == segundo) or (c == terceiro)):
        continue
    print(c, end=' | ')