# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que receba e divida 2 números. A saída da divisão
# precisará ser formatada com 4 casas decimais.
import os


resto = 0


class Calcular:
    def __init__(self, valor, valor1):
        self.valor = valor
        self.valor1 = valor1

    def dividir(self, valor, valor1):
        try:
            resto = float(valor) / float(valor1)
            return f'O resultado da divisão é: {resto:4f}'
        except ZeroDivisionError:
            return 'Impossível realizar divisão por zero!'
        except (TypeError, ValueError):
            return 'Insira apenas valores numéricos!'


while True:
    os.system('cls')
    menu = input('1 - Divisão | 0 - Sair: ')

    if menu == '1':
        valor = input('Insira o primeiro valor: ')
        valor1 = input('Insira o segundo valor: ')
        calcular = Calcular(valor, valor1)
        resultado = calcular.dividir(valor, valor1)
        input(f'{resultado}')

    elif menu == '0':
        break
