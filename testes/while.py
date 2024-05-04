import os


os.system('cls')

while True:
    valor = int(input('Insira um valor inteiro: '))
    resposta = ''

    if valor % 2 == 0:
        print()
        print(f'O {valor} é um número par.')
    else:
        print()
        print(f'O {valor} é um número ímpar.')
    
    print()        
    parada = input('Deseja sair do programa? ')
    if parada == 'sim':
        break
    else:
        os.system('cls')