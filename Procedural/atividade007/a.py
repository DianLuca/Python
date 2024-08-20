# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair).
import os


os.system('cls')

while True:
    notas = []
    print('O NÚMERO "0" SOZINHO ENCERRA O SISTEMA')
    entrada = input('Insira qualquer valor separado por vírgula: ').replace(' ','')
    
    valor = entrada.split(',')
    notas.extend(valor)

    if not (entrada == '0' or entrada.lower() == 's' in notas):
        print()
        for i in notas:
            print(i, end=', ')
        print()
    else:
        print()
        sair = input(
            'Valor 0 ou "s" identificado, deseja encerrar o sistema? [S - SIM]: ').lower()
        if sair == 's':
            break
        else:
            os.system('cls')
