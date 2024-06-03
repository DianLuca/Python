# Apenas um exercício próprio para fixação
import os


os.system('cls')

print('Exercício de contagem em um intervalo')
print()
print('-- SEJA BEM-VINDO --')
init = input('Deseja iniciar o programa?[s - sim] ').lower()
print()

while init == 's':
    print('Programa iniciado com sucesso')
    while True:
        a = int(input('Insira um número para iniciar o intervalo.: '))
        b = int(input('Insira um número para encerrar o intervalo: '))
        c = int(input('Insira os passos: '))
        print()

        if (a < b) and (c > 0): # crescente
            for d in range(a, (b + 1), c):
                print(d, end=' ')
        elif (a > b) and (c > 0): # Para caso seja inserido o valor para contagem crescente de forma inválida
            for d in range(b, (a + 1), c):
                print(d, end=' ')
        elif (a > b) and (c < 0): # decrescente
            c = 1
            for d in range(b, (a - 1), c):
                print(d, end=' ')
        elif (a < b) and (c < 0): # Para caso seja inserido o valor para contagem decrescente de forma inválida
            c = 1
            for d in range(a, (b - 1), c):
                print(d, end=' ')
        else:
            print(f'O intervalo possui apenas um número {a}')
        print()
        print('Fim do intervalo!')

        reset = input('Deseja contar novamente? [s - sim] ').lower()
        if reset == 's':
            os.system('cls')
        else:
            break
else:
    print('Fim do programa')
    os.system('cls')


# Adicionar validação para o caso de C < 0 e dividir as condições e o mesmo 
# para caso o valor seja = 0 
# Validar as entradas de valor, para que todos sejam valores númericos
# Mais ????