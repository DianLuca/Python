# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que receba um número qualquer e calcule o dobro e o triplo 
# desse número.
import os


class Operacao:
    def __init__(self, valor):
        self.valor = valor
    
    def multiplicar(self, valor):
        try:
            valor = float(valor)
            dobro = valor * 2
            triplo = valor * 3
            return f'O dobro e o triplo do valor {valor} são respectivamente: {dobro} e {triplo}'
        except (TypeError,ValueError):
            return 'Insira apenas valores numéricos! '

while True:
    os.system('cls')
    print('-' * 70)
    print('ENTRADA DE DADOS')
    print('-' * 70)

    # Entrada
    valor = input('Insira qualquer valor (s - Sair): ')
    if valor == 's':
        break
    else:
        operacao = Operacao(valor)
        resultado = operacao.multiplicar(valor)

    print('-' * 70)
    input(f'--- RESULTADO --- \n{resultado}\n' + '=' * 70)
    