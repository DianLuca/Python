# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que verifique se o usuário e senha estão inseridos em um
# banco de dados (fake). O usuário só terá acesso se digitar os dados corretos
# e, assim, sair do laço.
import os


class Login:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def exibir(self, usuario, senha):
        print('Variável sobrecarregada!')


class Verificacao(Login):
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def exibir(self):
        if self.usuario == 'admin' and self.senha == 'admin':
            input('Acesso concedido! ')
            return True
        else:
            input('Acesso negado! Tente novamente. ')
            return False


while True:
    os.system('cls')
    usuario = input('Insira o seu nome de usuário: ').strip()
    senha = input('Insira sua senha: ').strip()
    entrada = Verificacao(usuario, senha)
    status = entrada.exibir()
    if status == True:
        break
