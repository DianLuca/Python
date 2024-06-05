# Faça um programa que verifique se o usuário e senha estão inseridos em um
# banco de dados (fake). O usuário só terá acesso se digitar os dados corretos
# e, assim, sair do laço.
import os


os.system('cls')

usuario = input('Crie o seu nome de usuário: ')
senha = input('Crie uma senha: ')

banco = {'usuario': usuario, 'senha': senha}
os.system('cls')

usuario = input('Insira o seu nome de usuário: ')
senha = input('Insira sua senha: ')

if (banco['usuario'] == usuario and banco['senha'] == senha):
    print('Acesso concedido!')
else: 
    print('Acesso negado!')