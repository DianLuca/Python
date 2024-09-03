# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que converta metros em centímetros e milímetros.
import os


class Conversor:
    def __init__(self, metros):
        self.metros = metros

    def converter(self, metros):
        try:
            metros = float(metros)
            centimetros = metros * 100
            milimetros = metros * 1000
            return f'{metros} metros possuí em centímetros: {centimetros:.0f} cm e em milímetros: {milimetros:.0f} mm'
        except (TypeError, ValueError):
            return 'Insira apenas valores numéricos! '


while True:
    os.system('cls')

    print('-' * 70)
    print('ENTRADA DE DADOS')
    print('-' * 70)

    metros = input('Insira um valor em metros (s - Sair): ')

    if metros == 's':
        break
    else:
        conversor = Conversor(metros)
        resultado = conversor.converter(metros)

    print('-' * 70)
    input(f'--- RESULTADO --- \n{resultado}\n' + '=' * 70)
