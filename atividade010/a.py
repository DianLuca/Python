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


def ordenando(*lista_numeros):
    par = 0
    impar = 0
    for i in lista_numeros:
        i = int(i)
        if i % 2 == 0:
            pares.append(i)
            par += 1
        else:
            impares.append(i)
            impar += 1
    return par, impar


def adicinando_valores():
    while True:
        os.system('cls')
        valor = input('Adicione um valor: ').strip()
        lista_numeros.append(valor)
        continuar = input(
            'Deseja parar de inserir valores (S - Sim)? ').lower().strip()
        if continuar == 's' or (valor == '' and not valor.isnumeric()):
            break

while True:
    adicinando_valores()
    par, impar = ordenando(*lista_numeros)

    print(f'Existem {par} números pares são: {pares} ')
    print(f'Existem {impar} números pares são: {impares} ')

    input('Continue...')
    # Apagando os itens de todas as listas para inserir novos
    pares.clear() 
    impares.clear()
    lista_numeros.clear()
