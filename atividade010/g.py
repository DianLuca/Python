# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 12/07/2024

# Crie um programa que peça ao usuário 2 números maiores que 0 e menores que
# 11. Depois mostre um menu com as seguintes operações:
# 1. Soma: 2. Subtração : 3. Produto : 4. Divisão : 5. Divisão inteira :
# 6. Resto da divisão.
# O usuário deverá escolher um número maior ou  igual a 1 e menor ou igual a
# 6. Em seguida, você criará funções que retornem os resultados das operações,
# imprimindo os resultados na tela.
import os


os.system('cls')


# Função para realizar todos os cálculos
def calcular(operacao, a, b):
    # Casting
    a = float(a)
    b = float(b)
    if operacao == 'adição':
        return a + b 
    elif operacao == 'subtração':
        return a - b
    elif operacao == 'multiplicação':
        return a * b
    elif operacao == 'divisão':
        # Condicional para não permitir divisão por 0
        return a / b if b != 0 else 'Não é possível realizar divisão por 0, tente novamente!'
    elif operacao == 'divisão inteira':
        return a // b if b != 0 else 'Não é possível realizar divisão por 0, tente novamente!'
    else:
        return a % b if b != 0 else 'Não é possível realizar divisão por 0, tente novamente!'


while True:
    os.system('cls')
    print('|--- CALCULADORA ---|')
    menu = input(
        '1 - Soma | 2 - Subtração | 3 - Multiplicação | 4 - Divisão | '
        + '\n5 - Divisão Inteira | 6 - Resto da Divisão | 7 - Sair : ')

    if menu == '1':
        os.system('cls')
        operacao = 'adição'  # Operação que deseja realizar com base no menu
        print('ADIÇÃO')
        print('Insira números entre 0 e 11')
        # Utilizando list comprehension para inserir os valores
        valores = [input(f'Insira o {i+1}º valor: ') for i in range(2)]
        # Retorna os valores em índices
        resultado = calcular(operacao, valores[0], valores[1])
        print(resultado)
        input('Continue...')

    elif menu == '2':
        os.system('cls')
        operacao = 'subtração'
        print('SUBTRAÇÃO')
        print('Insira números entre 0 e 11')
        valores = [input(f'Insira o {i+1}º valor: ') for i in range(2)]
        resultado = calcular(operacao, valores[0], valores[1])
        print(resultado)
        input('Continue...')

    elif menu == '3':
        os.system('cls')
        operacao = 'multiplicação'
        print('MULTIPLICAÇÃO')
        print('Insira números entre 0 e 11')
        valores = [input(f'Insira o {i+1}º valor: ') for i in range(2)]
        resultado = calcular(operacao, valores[0], valores[1])
        print(resultado)
        input('Continue...')

    elif menu == '4':
        os.system('cls')
        operacao = 'divisão'
        print('DIVISÃO')
        print('Insira números entre 0 e 11')
        valores = [input(f'Insira o {i+1}º valor: ') for i in range(2)]
        resultado = calcular(operacao, valores[0], valores[1])
        print(resultado)
        input('Continue...')

    elif menu == '5':
        os.system('cls')
        operacao = 'divisão inteira'
        print('DIVISÃO INTEIRA')
        print('Insira números entre 0 e 11')
        valores = [input(f'Insira o {i+1}º valor: ') for i in range(2)]
        resultado = calcular(operacao, valores[0], valores[1])
        print(resultado)
        input('Continue...')

    elif menu == '6':
        os.system('cls')
        operacao = ''
        print('RESTO DA DIVISÃO')
        print('Insira números entre 0 e 11')
        valores = [input(f'Insira o {i+1}º valor: ') for i in range(2)]
        resultado = calcular(operacao, valores[0], valores[1])
        print(resultado)
        input('Continue...')

    elif menu == '7':
        break

    else:
        print()
        input('OPÇÃO INVÁLIDA, TENTE NOVAMENTE! ')
