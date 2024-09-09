# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que imprima os valores no intervalo definidos pelo usuário.
# Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos
# na tela.
import os


class Numeros:
    def __init__(self, inicio, fim, primeiro, segundo, terceiro):
        self.inicio = inicio
        self.fim = fim
        self.primeiro = primeiro
        self.segundo = segundo
        self.terceiro = terceiro

    def exibir(self, apresentar):
        print(apresentar, end=' | ')


class Intervalo(Numeros):
    def ignorar(self):
        try:
            for c in range(int(self.inicio), (int(self.fim) + 1)):
                if ((c == int(self.primeiro)) or (c == int(self.segundo)) or (c == int(self.terceiro))):
                    continue
                self.exibir(c)
        except (TypeError, ValueError):
            print('Insira apenas valores numéricos! ')


os.system('cls')

print('INSIRA UM INTERVALO E SELECIONE 3 NÚMEROS PARA IGNORAR')
print()
print('-- INTERVALO --')
inicial = input('Insira um número para iniciar.: ')
final = input('Insira um número para encerrar: ')
print('-- NÚMEROS IGNORADOS --')
primeiro = input('Insira o 1º número a ser ignorado: ')
segundo = input('Insira o 2º número a ser ignorado: ')
terceiro = input('Insira o 3º número a ser ignorado: ')

intervalo = Intervalo(inicial, final, primeiro, segundo, terceiro)
print('A lista com os valores ignorados:')
intervalo.ignorar()
