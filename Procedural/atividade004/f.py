# Faça um programa que receba o nome completo de uma pessoa e, posteriormente, 
# imprima esse nome separadamente.

import os


os.system('cls')

nome = input('Insira seu nome completo: ')

nome_completo = nome.split(' ')
print(nome_completo)
nome_separado = '-'.join(nome_completo)

print(nome_separado)