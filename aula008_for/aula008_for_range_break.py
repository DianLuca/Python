import os
import time


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE CONTROLE: BREAK')
print('=' * 70)

print()

for c in range(0, 10):
    time.sleep(c) # Apenas uma adição para teste
    print(f'Valor: {c}')
    
    # Condição para terminar a contagem
    if (c == 5):
        print(f'Contagem interrompida no {c}')
        break
    
print('-' * 70)
print('Fim do programa!')
print()