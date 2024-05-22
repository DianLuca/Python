# Faça um programa que leia o nome de uma pessoa e verifique se a palavra 
# 'Oliveira' está presente neste nome, mostrando True ou False. 
# .bool() retorna true or false

import os


os.system('cls')

nome = input('Insira um nome: ')

if 'Oliveira' in nome:
    print(bool('Oliveira'))
else:
    print(bool())