# Imports
import os
import time
# Outras bibliotecas
from datetime import datetime


os.system('cls')

while True: # Esse executa a parada do programa caso quiser
    n = 0 # Iniciando contador
    while True: # Esse faz a contagem e atualiza o tempo a cada segundo
        data = datetime.now()

        # Decalrando uma variável data formatada
        data_formatada = data.strftime('%d/%m/%Y %H:%M:%S')
        print(data_formatada)

        time.sleep(1)
        os.system('cls')
    
        if n >= 60:
            time.sleep(1)
            break # Fim da contagem
        n += 1 # Contador

    print(f'{data_formatada} e o sistema parou após {n} segundos')
    time.sleep(3)

    parada = input('Você deseja sair do programa?')
    
    if parada == 's':
        time.sleep(1)
        break # Fim da execução do sistema

os.system('cls')