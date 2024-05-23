# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 23/05/2024
# G) Faça um programa que leia o nome de um aluno e mostre quantas vezes a 
# letra 'o' aparece e em que posição ela aparece pela primeira e última vez.

import os


os.system('cls')

nome = input('Insira o seu nome: ').lower()

primeira_aparicacao = nome.find('o') + 1
ultima_aparicao = len(nome) - nome[::-1].find('o')

print(f'A primeira aparição da letra "o" é: {primeira_aparicacao}'
      + f' e da última: {ultima_aparicao}')