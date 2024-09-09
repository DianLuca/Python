# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que some a quantidade de números pares encontrados
# no intervalo entre 0 e 100.
import os


class Numeros:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def exibir(self, soma_pares, c_par):
        print(f'\nO somatório total do(s) {
              c_par} número(s) par(es) foi de: {soma_pares}.')


class Pares(Numeros):
    def pares(self):
        soma_pares = 0
        c_par = 0
        for c in range(self.inicio, (self.fim + 1)):
            if c % 2 == 0:
                soma_pares += c
                c_par += 1
                print(c, end=' | ')

        self.exibir(soma_pares, c_par)


os.system('cls')
print('SOMATÓRIO DE NÚMEROS PARES')
print()

a = int(input('Insira o menor número: '))
b = int(input('Insira o maior número: '))
print()

numeros = Pares(a, b)
numeros.pares()
