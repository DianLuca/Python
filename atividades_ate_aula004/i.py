# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 19/04/2024
# Faça um programa que receba um valor em reais, depois calcule quantos 
# dólares daria para comprar com esse valor.

# Imports
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
valor_real = float(input('Insira um valor em reais para conversão: '))

# Processamento
valor_dolar = 5.20 # Cotação de 19/04/2024

conversao_real_dolar = valor_dolar * valor_real
conversao_dolar_real = valor_real / valor_dolar

# Saída
print('-' * 70)
print('--- CONVERSÃO DE VALORES')
print('=' * 70)
print(f'Um dólar corresponde a: R$ {conversao_real_dolar:.2f} e '
      + f'R${valor_real:.2f} correspondem a: $ {conversao_dolar_real:.2f}' 
      + f'(dólares)')