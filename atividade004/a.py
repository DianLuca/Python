# Faça um programa que solicite separadamente o nome, o nome do meio e o 
# sobrenome de uma pessoa. Em seguida, imprima o nome completo.

import os


os.system('cls')

nome = input('Insira seu nome: ')
nome_meio = input('Insira o nome do meio: ')
sobrenome = input('Insira seu sobrenome: ')
resposta = ''

# Validação
if (nome and nome_meio and sobrenome) == str:
    lista = [nome, nome_meio, sobrenome]
    juncao = ' '.join(lista)
    resposta = (f'O seu nome completo é: {juncao}')
else:
    resposta = (f'Um dos valores inseridos é inválido, por favor insira apenas ' 
          + f'valores do tipo texto.')
    
print()
print(resposta)
