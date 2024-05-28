# Faça um programa que leia o nome de uma pessoa e verifique se a palavra 
# 'Oliveira' está presente neste nome, mostrando True ou False. 
# .bool() retorna true or false

import os


os.system('cls')

nome = input('Insira um nome: ').lower()

if not (nome.replace(' ','').isalpha()):
    print('Um dos caracteres inserir é inválido.')
else:
    if 'oliveira' in nome:
        print(f'{bool(True)}. Foi encontrado {nome.title()} no nome.')
    else:
        print(f'{bool(False)}. Não foi encontrado "Oliveira" no nome.')