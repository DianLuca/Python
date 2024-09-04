# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que receba um número inteiro e mostre o sucessor
# e antecessor.
import os


class Adjacentes:
    def __init__(self, valor):
        self.valor = valor

    def sucessor_antecessor(self):
        try:
            self.valor = float(self.valor)
            antecessor = self.valor - 1
            sucessor = self.valor + 1
            return f'O antessessor e o sucessor do valor: {self.valor}, são os seguintes respectivamentes: {antecessor} e {sucessor}'
        except (TypeError, ValueError):
            return 'Insira apenas valores numéricos! '


while True:
    os.system('cls')

    print('-' * 70)
    print('ENTRADA DE DADOS')
    print('-' * 70)

    # Entrada
    valor = input('Insira um valor (s - Sair): ')
    if valor == 's':
        break
    else:
        adjacentes = Adjacentes(valor)
        resultado = adjacentes.sucessor_antecessor()
        input(resultado)
