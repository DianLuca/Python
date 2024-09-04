# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que receba e divida 2 números. A saída da divisão
# precisará ser formatada com 4 casas decimais.
import os


resto = 0


class Calcular:
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor

    def dividir(self):
        try:
            quociente = float(self.dividendo) / float(self.divisor)
            return f'O resultado da divisão é: {quociente:.4f}'
        except ZeroDivisionError:
            return 'Impossível realizar divisão por zero!'
        except (TypeError, ValueError):
            return 'Insira apenas valores numéricos!'


while True:
    os.system('cls')
    menu = input('1 - Divisão | 0 - Sair: ')

    if menu == '1':
        dividendo = input('Insira o primeiro dividendo: ')
        divisor = input('Insira o segundo divisor: ')
        calcular = Calcular(dividendo, divisor)
        resultado = calcular.dividir()
        input(f'{resultado}')

    elif menu == '0':
        break
