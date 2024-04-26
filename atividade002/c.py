import os


os.system('cls')

velocidade_usuario = int(input('Insira a velocidade (Km/h): '))
resposta = ''
velocidade_limite = 60

if velocidade_usuario < velocidade_limite:
    resposta = f'Você está dirigindo dentro da velocidade permitida.'
elif velocidade_usuario == velocidade_limite:
    resposta = f'Você está no limite de velocidade permitido.'
else:
    resposta = f'A velocidade máxima permitida da via é {velocidade_limite} Km/h, reduza a velocidade.'
    
print('-' * 70)
print(resposta)
print()