# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que peça 3 valores , depois calcule e imprima  a
# soma e a multiplicação desses valores.
import os


class Calcular:
    def __init__(self, valor, valor1, valor2):
        self.valor = valor
        self.valor1 = valor1
        self.valor2 = valor2

    def somar(self, valor, valor1, valor2):
        try:
            soma = float(valor) + float(valor1) + float(valor2)
            return f'O Resultado da soma dos 3 valores: {soma}.'
        except (TypeError, ValueError):
            return 'Insira apenas valores numéricos'

    def multiplicar(self, valor, valor1, valor2):
        try:
            multiplica = float(valor) * float(valor1) * float(valor2)
            return f'O Resultado da multiplicação dos 3 valores: {multiplica}'
        except (TypeError, ValueError):
            return 'Insira apenas valores numéricos'


while True:
    os.system('cls')
    menu = input('1 - Soma | 2 - Multiplicar | 0 - Sair: ')

    if menu == '1':
        print('--- ADIÇÃO ---')
        valor = input('Insira o primeiro para adicionar: ')
        valor1 = input('Insira o segundo para adicionar: ')
        valor2 = input('Insira o terceiro para adicionar: ')
        calcular = Calcular(valor, valor1, valor2)
        resultado = calcular.somar(valor, valor1, valor2)
        input(resultado)

    elif menu == '2':
        print('--- MULTIPLICAÇÃO ---')
        valor = input('Insira o primeiro para multiplicar: ')
        valor1 = input('Insira o segundo para multiplicar: ')
        valor2 = input('Insira o terceiro para multiplicar: ')
        calcular = Calcular(valor, valor1, valor2)
        resultado = calcular.multiplicar(valor, valor1, valor2)
        input(resultado)

    elif menu == '0':
        print('Programa encerrado!')
        break
