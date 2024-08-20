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


while True:
    os.system('cls')
    print('|--- CALCULANDO O IMC ---|')
    menu = input('1 - IMC | 0 - Sair: ')
    if menu == '1':
        os.system('cls')
        print('|--- CALCULANDO O IMC ---|')
        peso = input('Insira o seu peso: ').strip()
        altura = input('Insira o seu altura: ').replace(',', '.').strip()

        imc = calcular(altura, peso)
        print(f'Altura: {altura} m \nPeso: {peso} Kg \nIMC: {imc:.2f}')
        input('Pressione qualquer tecla para voltar ao menu. ')
    elif menu == '0':
        print('Programa finalizado!')
        break
