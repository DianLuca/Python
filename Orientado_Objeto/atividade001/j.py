# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa com entrada de dados para calcular o perímetro de um retângulo.
import os


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_perimetro(self):
        try:
            self.base = float(self.base)
            self.altura = float(self.altura)
            perimetro_retangulo = 2*(self.base + self.altura)
            return f'O perímetro de um retângulo de base: {self.base:.2f} cm e altura: {self.altura:.2f} cm é de: {perimetro_retangulo:.2f} cm'
        except (TypeError, ValueError):
            return 'Insira apenas valores numéricos! '


while True:
    os.system('cls')

    print('-' * 70)
    print('ENTRADA DE DADOS')
    print('-' * 70)

    menu = input('1 - Calcular o perímetro de um retângulo | 0 - Sair: ')
    if menu == '1':
        base = input('Insira a base do retângulo (em cm): ')
        altura = input('Insira a altura do retângulo (em cm): ')
        retangulo = Retangulo(base, altura)
        perimetro = retangulo.calcular_perimetro()
        print('-' * 70)
        print('-- RESULTADO --')
        input(f'{perimetro}\n' + '=' * 70)

    elif menu == '0':
        break
