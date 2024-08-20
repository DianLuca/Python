import os


os.system('cls')

# Definindo uma função
def calcular_velocidade_media(distancia, tempo):
    #Vm = ΔS/Δt
    if distancia < 1000:
        dividendo_distancia = distancia / 1000
    else:
        dividendo_distancia = distancia
        
    if tempo < 60:
        dividendo_tempo = tempo
    else:
        dividendo_tempo = tempo / 60
        
    velocidade_media = (dividendo_distancia) / (dividendo_tempo)
    return velocidade_media


distancia = float(input('Digite a distância percorrida (em km): '))
tempo = float(input('Digite a tempo gasto (em horas): '))


# Calcular a velocidade média usando a função criada
velocidade = calcular_velocidade_media(distancia, tempo)

# Exibir o resultado
print(f'A velocidade média é {velocidade:.2f}km/h.')