# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# Faça um programa que leia as vogais, depois mostre-as em ordem inversa.
import os


os.system('cls')

vogais = []

entrada = input('Insira as vogais separadas por vírgula: ').replace(' ','')

letras = entrada.split(',')
vogais.extend(letras)

vogais.sort(reverse = True) # Sempre irá retornar os itens na ordem desejada, independente de posição
print()
print(f'As vogais em ordem contaria: {vogais}')