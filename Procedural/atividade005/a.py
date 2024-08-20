# Faça um programa que imprima os números no intervalo entre 1 e 100. 
# Os números devem ser apresentados na horizontal.

import os 


os.system('cls')


c = 0

for c in range(1, 101):
    print(c, end = ' - ')
    c += 1