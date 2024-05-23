# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 23/05/2024
# I) Faça um programa que receba o nome completo de uma pessoa e, 
# em seguida, mostre o primeiro e o último nome.

import os


os.system('cls')

nome_completo = input('Insira seu nome completo: ')

lista = nome_completo.split()
primeiro_nome = lista[0]
ultimo_nome = lista[-1]

print(f'Primeiro Nome: {primeiro_nome} \nÚltimo Nome..: {ultimo_nome}')