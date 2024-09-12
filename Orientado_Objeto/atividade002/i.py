# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida,
# solicite ao usuário digitar uma letra. Caso a letra seja o “f" finalize
# a aplicação. Do contrário, imprima novamente a mesma frase até que o
# caractere “f" seja digitado.
import os
import time


class Operacao:
    def __init__(self, parada):
        self.parada = parada
        
    def parar(self, parada):
        print()


class Funcionamento(Operacao):
    def __init__(self, parada):
        self.parada = parada

    def parar(self):
        print('Estou em looping!')
        time.sleep(2)
        if self.parada != 'f':
            return False, ''
        else:
            return True, 'Encerrando looping!'


while True:
    os.system('cls')
    parada = input('Deseja finalizar o programa [f - sim]? ').lower()
    funcionamento = Funcionamento(parada)
    finalizar, mensagem = funcionamento.parar()
    if finalizar == True:
        print(mensagem)
        break
