# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 19/04/2024
# Faça um programa que peça o ano do seu nascimento e calcule a sua idade.
import os
import datetime


class Idade:
    def __init__(self, ano_nascimento):
        self.ano_nascimento = ano_nascimento

    def calcular_idade(self):
        ano_atual = datetime.datetime.now().year
        idade = int(ano_atual) - self.ano_nascimento
        return idade


while True:
    os.system('cls')
    ano_nascimento = int(input('Insira seu ano de nascimento: '))
    idade = Idade(ano_nascimento)
    resultado = idade.calcular_idade()
    input(f'Sua idade atual é: {resultado} ano(s)')
    break
