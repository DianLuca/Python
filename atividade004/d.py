# Faça um programa que leia uma frase e depois exiba na tela:
# • A frase em minúsculas, a frase em maiúsculas, a quantidade
# de caracteres na frase e quantas letras tem a 2ª palavra na frase.

import os


os.system('cls')

frase = input('Insira uma frase qualquer: ')

print(frase)

minuscula = frase.lower()
maiuscula = frase.upper()
contagem = len(frase)

print(f'A frase toda minúscula será: "{minuscula}", toda maiúscula: '
      + f'"{maiuscula}" e possui {contagem} caracteres.')

lista = frase.split(' ')
palavra = ''.join(lista[1:2])
contagem_segunda_palavra = len(palavra)
print(f'A segunda palavra da frase é: {lista[1:2]} e possui: '
      + f'{contagem_segunda_palavra}  caracteres.')
