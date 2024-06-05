# Crie um programa que realiza a contagem de 1 até 100, usando apenas de 
# números ímpares, ao final do processo exiba na tela quantos números ímpares
# foram encontrados nesse intervalo, assim como a soma dos mesmos.
import os


os.system('cls')

print('NÚMEROS ÍMPARES EM UM INTERVALO E SUA QUANTIDADE')
inicio = int(input('Insira um valor inteiro para iniciar o intervalo: '))
final = int(input('Insira um valor inteiro para finalizar o intervalo: '))

c_impar = 0

for c in range(inicio, (final +1)):
    
    if (c % 2 != 0) == True:
        print(c, end=' ')
        
    
    