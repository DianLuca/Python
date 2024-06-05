# Apenas um exercício próprio para fixação
import os
import time # Para adicionar tempo para execução do programa
import numpy as np # Para me permitir utilizar valores decimais para contagem dos intervalos


os.system('cls')

print('Exercício de contagem em um intervalo')
print()
print('-- SEJA BEM-VINDO --')
init = input('Deseja iniciar o programa?[s - sim] ').lower() # Input para iniciar o programa
print()

while init == 's':
    print('Aguarde!')
    time.sleep(3)
    print('Programa iniciado com sucesso')
    while True:
        a = int(input('Insira um número para iniciar o intervalo.: ')) # Variável para iniciar
        b = int(input('Insira um número para encerrar o intervalo: ')) # Variável para finalizar
        c = float(input('Insira os passos: ')) # Passos a serem contados
        print()

        if c > 0: # contagem crecente
            if (a < b):
                for d in np.arange(a, (b + .1), c): # .1 inserido para evitar erros na contagem
                    print(d, end=' ')
            else: # Para caso seja inserido o valor para contagem crescente de forma inválida
                for d in np.arange(b, (a + .1), c): 
                    print(d, end=' ')
        elif c < 0: # contagem decrescente
            if (a > b): # Para caso seja inserido o valor para contagem decrescente de forma inválida
                for d in np.arange(a, (b - .1), c):
                    print(d, end=' ')
            else: 
                for d in np.arange(b, (a - .1), c):
                    print(d, end=' ')
        else:
            print(f'O intervalo possui passo igual a {c}, insira um passo' 
                  + f'maior ou menor para executar a operação.')
        print()
        print('Fim do intervalo!')

        reset = input('Deseja contar novamente? [s - sim] ').lower() # Input para parada de contagem
        if reset != 's':
            fechar = input('Deseja finalizar o programa? [s - sim] ').lower() # Input para encerrar o sistema
            os.system('cls')
            if fechar == 's':
                os.system('cls')
                break
        else:
            os.system('cls')
    print('Fim do programa!')
    time.sleep(3)
    os.system('cls')
    break      
else:
    print('Fim do programa!')
    time.sleep(3)
    os.system('cls')


# Adicionar validação para o caso de C < 0 e dividir as condições e o mesmo 
# para caso o valor seja = 0 - REALIZADO
# Validar as entradas de valor, para que todos sejam valores válidos para às entradas
# Mais ????