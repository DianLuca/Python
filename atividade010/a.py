# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 12/07/2024

# Crie uma função que receba uma lista de números. Depois retorne duas listas
# com os números pares, os números ímpares, a quantidade de números pares e a
# quantidade de números ímpares.
import os


os.system('cls')

lista_numeros = []
pares = []
impares = []


def adicinando_valores(valor):
    lista_numeros.extend(valor)


def ordenando(*lista_numeros):
    for i in lista_numeros:
        i = int(i)
        pares.append(i) if i % 2 == 0 else impares.append(i)


while True:
    os.system('cls')
    valor = input('Adicione um valor: ').strip()
    adicinando_valores(valor)
    ordenando(valor)
    par, impar = len(pares), len(impares)

    print(f'Existem {par} números pares são: {pares} ')
    print(f'Existem {impar} números impares são: {impares} ')

    input('Continue...')
    continuar = input(
        'Deseja parar de inserir valores (S - Sim)? ').lower().strip()
    if continuar == 's' or (valor == '' and not valor.isnumeric()):
        break
