# Faça um programa que solicite separadamente o nome, o nome do meio e o 
# sobrenome de uma pessoa. Em seguida, imprima o nome completo.

import os


os.system('cls')

nome = input('Insira seu nome: ')
nome_meio = input('Insira o nome do meio: ')
sobrenome = input('Insira seu sobrenome: ')
resposta = ''

lista = [nome, nome_meio, sobrenome]
juncao = " ".join(lista)
    
# Validação
if not (nome.replace(' ','').isalpha() and nome_meio.replace(' ','').isalpha()
        and sobrenome.replace(' ','').isalpha()):
    resposta = (f'Caracter inválido, digite somente letras!!!!')
else:
    resposta = (f'A junção das strings ficam: {juncao}')

print()
print(resposta)