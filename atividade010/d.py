# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 12/07/2024

# Crie uma função que receba uma temperatura em fahrenheit e retorne o valor
# em graus célsius.
import os


os.system('cls')


def converter(fahrenheit):
    fahrenheit = float(fahrenheit)
    fahrenheit_celsius = (fahrenheit - 32) * (5/9)
    return fahrenheit_celsius


fahrenheit = input('Insira a temperatura em fahrenheit: ')
celcius = converter(fahrenheit)

print(f'{fahrenheit}°F = {celcius}°C')
