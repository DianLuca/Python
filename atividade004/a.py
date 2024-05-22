# Faça um programa que solicite separadamente o nome, o nome do meio e o 
# sobrenome de uma pessoa. Em seguida, imprima o nome completo.

import os


os.system('cls')

nome = input('Insira seu nome: ')
nome_meio = input('Insira o nome do meio: ')
sobrenome = input('Insira seu sobrenome: ')

lista = [nome, nome_meio, sobrenome]
juncao = ' '.join(lista)
print(f'O seu nome completo é: {juncao}')