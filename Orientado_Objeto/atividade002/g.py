# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que calcule os números primos em um intervalo
# pré-determinado pelo usuário.
import os


class Numeros:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def exibir(self, primos):
        print(f'Esses são os números primos de {
              self.inicio} a {self.fim}: {primos}')


class Primos(Numeros):
    def encontrar_primos(self):
        try:
            if self.inicio < 2:
                print(f'Não existe número primo de {self.inicio}, portando '
                      + f'adotaremos o menor mais próximo: 2.')
                self.inicio = 2
            for c in range(self.inicio, (self.fim + 1)):  # O número 0 e 1 não são primos
                for i in range(self.inicio, c):  # O primeiro número primo é 2, então a >= 2
                    if c % i == 0:
                        break
                else:
                    self.exibir(c)
        except (TypeError, ValueError):
            print('Insira apenas valores numéricos. ')


os.system('cls')
print('NÚMEROS PRIMOS')
print()

a = input('Insira um número para começar: ')  # vide linha 21
b = input('Insira um número para finalizar: ')
print()
primo = Primos(a, b)
primo.encontrar_primos()
