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

    def calcular_media(self):
        try:
            if (float(self.nota) < 0 or float(self.nota1) < 0 or float(self.nota2) < 0 or float(self.nota3) < 0):
                return 'Favor inserir valores maiores ou iguais a zero! '
            else:
                total_notas = float(self.nota) + float(self.nota1) + \
                    float(self.nota2) + float(self.nota3)
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
        resultado = notas.calcular_media()
        input(resultado)

    elif menu == '0':
        break
