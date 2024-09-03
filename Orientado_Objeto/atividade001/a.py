# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que peça 3 valores , depois calcule e imprima  a 
# soma e a multiplicação desses valores.
import os


# def validar_numero(*valor):
#     if (valor[0] and valor[1] and valor[2]) != (float or int):
#         input('Insira apenas valores numéricos!')
#         return 
        
    

class Calcular:
    def __init__(self, valor, valor1, valor2):
        self.valor = valor
        self.valor1 = valor1
        self.valor2 = valor2
        
    def somar(self, valor, valor1, valor2):
        soma = valor + valor1 + valor2
        return soma
    
    def multiplicar(self, valor, valor1, valor2):
        multiplica = valor * valor1 * valor2
        return multiplica
    
while True:
    os.system('cls')
    menu = input ('1 - Soma | 2 - Multiplicar | 0 - Sair: ')
    
    if menu == '1':
        print('--- ADIÇÃO ---')
        valor = input('Insira o primeiro para adicionar: ')
        valor1 = input('Insira o segundo para adicionar: ')
        valor2 = input('Insira o terceiro para adicionar: ')
        # validar_numero(valor, valor1, valor2)
        calcular = Calcular(valor, valor1, valor2)
        resultado = calcular.somar(valor, valor1, valor2)
        input(f'O Resultado da soma dos 3 valores: {resultado}.')
    
    if menu == '2':
        print('--- MULTIPLICAÇÃO ---')
        valor = input('Insira o primeiro para multiplicar: ')
        valor1 = input('Insira o segundo para multiplicar: ')
        valor2 = input('Insira o terceiro para multiplicar: ')
        # validar_numero(valor, valor1, valor2)
        calcular = Calcular(valor, valor1, valor2)
        resultado = calcular.multiplicar(valor, valor1, valor2)
        input(f'O Resultado da multiplicação dos 3 valores: {resultado}.')
    
    if menu == '0':
        print('Programa encerrado!')
        break
        
