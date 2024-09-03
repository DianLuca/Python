# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que peça 4 notas, após a entrada de dados calcular a
# média das notas digitadas.
import os


total_notas = 0


class Notas:
    def __init__(self, nota, nota1, nota2, nota3):
        self.nota = nota
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_media(self, nota, nota1, nota2, nota3):
        try:
            total_notas = float(nota) + float(nota1) + \
                float(nota2) + float(nota3)
            media = total_notas / 4
            return f'A média das notas foi: {media}'
        except ZeroDivisionError:
            return 'Impossível realizar divisão por zero! '
        except (TypeError, ValueError):
            return 'Insira apenas valores numéricos!'


while True:
    os.system('cls')
    menu = input('1 - Calcular Média | 0 - Sair: ')

    if menu == '1':
        print('--- Média de 4 notas ---')
        nota = input('Insira o valor da primeira nota: ')
        nota1 = input('Insira o valor da segunda nota: ')
        nota2 = input('Insira o valor da terceira nota: ')
        nota3 = input('Insira o valor da quarta nota: ')
        notas = Notas(nota, nota1, nota2, nota3)
        resultado = notas.calcular_media(nota, nota1, nota2, nota3)
        input(resultado)

    elif menu == '0':
        break
