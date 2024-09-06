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


while True:
    print('Estou em looping')
    time.sleep(2)
    print()
    parada = input('Deseja finalizar o programa [f - sim]? ').lower()
    
    if  parada == 'f':
        break

os.system('cls')