# Imports
import os
# Outras bibliotecas
from datetime import datetime 
from datetime import date


os.system('cls')

data = datetime.now()

# Decalrando uma variável data formatada
data_formatada = data.strftime('%d/%m/%Y') 

# Declarando uma variável data e hora formatada
data_hora_formatado = data.strftime('%d/%m/%Y %H:%M')

print(f'Data foramtada: {data_formatada}')
print(f'Data e hora formatadas: {data_hora_formatado}')

data_atual = date.today()
nascimento = 1970
idade = data_atual.year - nascimento

# Imprimindo a data atual e o nascimento
print('-' * 70)
print(f'Data atual do sistema: {data_atual}')
print(f'Nascimento...........: {nascimento}')
# Imprimindo só o ano
print(f'Ano atual............: {data_atual.year}')
# Imprimindo só a idade
print(f'Sua idade é..........: {idade} anos')
print('-' * 70)