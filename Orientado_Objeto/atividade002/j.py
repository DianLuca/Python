# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Crie um programa que realiza a contagem de 1 até 100, usando apenas de
# números ímpares, ao final do processo exiba na tela quantos números ímpares
# foram encontrados nesse intervalo, assim como a soma dos mesmos.
import os


class Numeros:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def exibir(self, c_impar, somatorio):
        print('Sobrecarregando variável.')


class Impares(Numeros):
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def exibir(self):
        try:
            c_impar = 0
            somatorio = 0
            for c in range(int(self.inicio), (int(self.fim) + 1)):
                if c % 2 != 0:
                    print(c, end=' | ')
                    c_impar += 1
                    somatorio += c
            print(f'\nExiste {c_impar} número(s) ímpar(es) nesse intervalo. '
                  + f'A soma de todos os valores é igual a: {somatorio}')
        except (TypeError, ValueError):
            print('Insira apenas valores númericos e inteiros! ')


os.system('cls')

print('NÚMEROS ÍMPARES EM UM INTERVALO E SUA QUANTIDADE E SOMA TOTAL')
inicio = input('Insira um valor inteiro para iniciar o intervalo..: ')
final = input('Insira um valor inteiro para finalizar o intervalo: ')
print()
impar = Impares(inicio, final)
impar.exibir()
