# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Crie um programa que pede que o usuário digite um nome ou uma frase,
# verifique se esse conteúdo digitado é um palíndromo ou não, exibindo
# em tela esse resultado.
import os


class Palavra():
    def __init__(self, entrada):
        self.palavra = entrada

    def exibir(self, entrada):
        print('Sobrecarregando variável.')


class Palindromo(Palavra):
    def __init__(self, entrada):
        self.palavra = entrada

    def exibir(self):
        palindromo = self.palavra[::-1]
        if self.palavra == palindromo:
<<<<<<< HEAD
            self.exibir(f'A palavra {self.palavra} é um palíndromo, pois {
                        self.palavra} ao contrário: "{palindromo}" ficam iguais!')
        else:
            self.exibir(f'A palavra {self.palavra} não é um palíndromo, pois {
                        self.palavra} ao contrário: "{palindromo}" não são iguais!')
=======
            print(
                f'A palavra {self.palavra} é um palíndromo, pois {self.palavra} ao contrário: "{palindromo}" ficam iguais!')
        else:
            print(
                f'A palavra {self.palavra} não é um palíndromo, pois {self.palavra} ao contrário: "{palindromo}" não são iguais!')
>>>>>>> 209ad2551d906d77631dccae4239f87c4a23f5af


os.system('cls')

print('-- VERIFICAÇÃO DE PALÍNDROMO --')  # Quando um nome ou uma frase é
# igual mesmo ao contrário
nome = input('Insira seu nome ou uma frase: ').strip().lower()
palindromo = Palindromo(nome)
<<<<<<< HEAD
palindromo.verificar()
=======
palindromo.exibir()
>>>>>>> 209ad2551d906d77631dccae4239f87c4a23f5af
