# SISTEMA PARA FINS DIDATICOS PODE POSSUIR ALGUNS ERROS. FORAM UTILIZADOS CONCEITOS 
# APRENDIDOS ATÉ O MOMENTO, OUTROS CONCEITOS PODEM SER UTILIZADOS FUTURAMENTE. 
# POSSÍVEIS ALTERAÇÕES PODEM SER INSERIDAS. DICAS SÃO BEM-VINDAS.
# POR: Dian Luca Valente Nascimento - em 05/06/2024 (Última atualização).

# Apenas um exercício próprio para fixação
import os
import time  # Para adicionar tempo para execução do programa
import numpy as np # Para me permitir utilizar valores decimais para contagem dos intervalos


os.system('cls')

print('Exercício de contagem em um intervalo')
print()
print('-- SEJA BEM-VINDO --')
# Input para iniciar o programa
init = input('Deseja iniciar o programa?[s - sim] ').lower()
print()

while init == 's':
    print('Aguarde!')
    time.sleep(3)
    print('Programa iniciado com sucesso')
    while True:
        a = input('Insira um número para iniciar o intervalo.: ') # Variável para iniciar
        b = input('Insira um número para encerrar o intervalo: ') # Variável para finalizar
        c = input('Insira os passos: ')  # Passos a serem contados
        print()

        # Validação dos valores inseridos
        if not ((a.lstrip('-').replace('.', '').isdigit()) and 
                (b.lstrip('-').replace('.', '').isdigit()) and 
                (c.lstrip('-').replace('.', '').isdigit())):
                # lstrip está removendo o sinal(-) apenas para realizar a 
                # verificação e replace remove o ponto(.) pelo mesmo motivo
            print('O item possui um caracter inválido! Insira apenas números.')
            print()
        else:
            a = float(a)
            b = float(b) # Casting para poder usar as variáveis de forma correta
            c = float(c)
            
            if c > 0:  # contagem crecente
                if (a < b):
                    # .1 inserido para evitar erros na contagem,
                    for d in np.arange(a, (b + .1), c):
                        # mas apresenta erro em contas decimais
                        print(round(d, 4), end=' ')
                else:  # Para caso seja inserido o valor para contagem crescente de forma inválida
                    for d in np.arange(b, (a + .1), c):
                        print(round(d, 4), end=' ')
            elif c < 0:  # contagem decrescente
                if (a > b):
                    for d in np.arange(a, (b - .1), c):
                        print(round(d, 4), end=' ')
                else:  # Para caso seja inserido o valor para contagem decrescente de forma inválida
                    for d in np.arange(b, (a - .1), c):
                        print(round(d, 4), end=' ')
            else:
                print(f'O intervalo possui passo igual a {c}, insira um passo'
                  + f'maior ou menor para executar a operação.')
            print()
            print('Fim do intervalo!')

        # Input para parada de contagem
        reset = input('Deseja contar novamente? [s - sim] ').lower()
        if reset != 's':
            # Input para encerrar o sistema
            fechar = input('Deseja finalizar o programa? [s - sim] ').lower()
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
