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

    def exibir(self, inicio, fim):
        print(f'Sobrecarregando variável.')


class Primos(Numeros):
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def exibir(self):
        try:
<<<<<<< HEAD
            if self.inicio < 2:
                print(f'Não existe número primo de {self.inicio}, portando '
=======
            if int(self.inicio) < 2:
                print(f'Não existe número primo de {int(self.inicio)}, portando '
>>>>>>> 209ad2551d906d77631dccae4239f87c4a23f5af
                      + f'adotaremos o menor mais próximo: 2.')
                self.inicio = 2
            for c in range(int(self.inicio), (int(self.fim) + 1)):  # O número 0 e 1 não são primos
                for i in range(int(self.inicio), c):  # O primeiro número primo é 2, então a >= 2
                    if c % i == 0:
                        break
                else:
                    print(c, end=' | ')
        except (TypeError, ValueError):
            print('Insira apenas valores numéricos. ')


os.system('cls')
print('NÚMEROS PRIMOS')
print()

a = input('Insira um número para começar: ')  # vide linha 21
b = input('Insira um número para finalizar: ')
print()
primo = Primos(a, b)
primo.exibir()
