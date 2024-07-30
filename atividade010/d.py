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


while True:
    os.system('cls')
    print('|--- CONVERSOR DE TEMPERATURA ---|')
    menu = input('1 - FAHRENHEIT -> CELSIUS | 0 - SAIR : ')

    if menu == '1':
        os.system('cls')
        print('CONVERTENDO FAHRENHEIT -> CELSIUS')
        fahrenheit = input('Insira a temperatura em fahrenheit: ')
        celcius = converter(fahrenheit)

        print(f'{fahrenheit}°F = {celcius}°C')
        input('Pressione qualquer tecla para voltar ao menu. ')

    elif menu == '0':
        print('Programa finalizado!')
        break
