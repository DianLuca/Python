# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 12/07/2024

# Crie uma função que receba a altura e o peso de uma pessoa. Depois retorne 
# o seu IMC.
import os


os.system('cls')

def calcular(altura, peso):
    altura = float(altura)
    peso = float(peso)
    calcula_imc = (peso / (altura**2))
    return calcula_imc

peso = input('Insira o seu peso: ')
altura = input('Insira o seu altura: ')

imc = calcular(altura, peso)

print(f'Altura: {altura} m \nPeso: {peso} Kg \nIMC: {imc:.2f}')