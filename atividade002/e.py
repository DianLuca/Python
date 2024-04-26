import os


os.system('cls')

distancia_usuario = float(input('Insira a distância desejada para a viagem: '))
resposta = ''
distancia_200 = 0.7  # R$ 0,70
distancia_maior_200 = 0.4  # R$ 0,40

if 0 < distancia_usuario <= 200:
    valor_total = distancia_200 * distancia_usuario
    resposta = (f'O valor da sua viagem de {distancia_usuario} KM será de: ' 
    + f'R$ {valor_total:.2f}')
elif distancia_usuario > 200:
    valor_total = distancia_maior_200 * distancia_usuario
    resposta = (f'O valor da sua viagem de {distancia_usuario} KM será de: '
    + f'R$ {valor_total:.2f}')
else:
    resposta = f'Você não irá realizar uma viagem'

print()
print(resposta)
print('-' * 70)