# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 23/05/2024
# G) Faça um programa que leia o nome de um aluno e mostre quantas vezes a 
# letra 'o' aparece e em que posição ela aparece pela primeira e última vez.

import os


os.system('cls')

nome = input('Insira o seu nome: ').lower()

primeira_aparicao = nome.find('o') + 1
ultima_aparicao = nome.rfind('o') + 1

print(f'A primeira aparição da letra "o" é: {primeira_aparicacao}'
      + f' e da última: {ultima_aparicao}')