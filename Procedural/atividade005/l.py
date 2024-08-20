# Faça um programa que verifique se o usuário e senha estão inseridos em um
# banco de dados (fake). O usuário só terá acesso se digitar os dados corretos
# e, assim, sair do laço.
import os


os.system('cls')


while True:
    usuario = input('Insira o seu nome de usuário: ')
    senha = input('Insira sua senha: ')
    
    if (usuario == 'admin' and senha == 'admin'):
        print('Acesso concedido!')
        break
    else: 
        print('Acesso negado! Tente novamente')