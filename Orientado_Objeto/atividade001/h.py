# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que receba um número inteiro, depois imprima sua
# tabuada de multiplicação.
import os


class Tabuada:
    def __init__(self, numero):
        self.numero = numero

    def multiplicar(self):
        try:
            self.numero = int(self.numero)
            for i in range(1, 11):
                resultado = self.numero * i
                print(f'{self.numero} x {i} = {resultado}', end='\n')

        except (TypeError, ValueError):
            return 'Insira apenas valores inteiros e numéricos! '


while True:
    os.system('cls')
    menu = input('1 - Tabuada | 0 - Sair: ')

    if menu == '1':
        numero = input('Insira um número inteiro: ')
        tabuada = Tabuada(numero)
        print(f'Tabuada completa no número {numero}:')
        resultado = tabuada.multiplicar()
        print()
        input('Pressione qualquer tecla para voltar ao menu: ')

    elif menu == '0':
        break
