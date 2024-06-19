import os
import tabulate


os.system('cls')

carta_vinho = [  # EXEMPLO DE COMO DEVE SER:
    {'Categoria': 'Tinto', 'País': 'Brasil', 'Preço': 25.99, 'Descrição': 'Marca: Miolo Wine Group. '
     'Este vinho apresenta-se equilibrado, redondo com final de boca agradável.'}
]

carta_vinho = [{**{'':i + 1}, **row} for i, row in enumerate(carta_vinho)]
# {**{'': i + 1}, **row}: Aqui, estamos criando um novo dicionário para cada 
# item em carta_vinho. Vamos dividir isso em duas partes:

# {'': i + 1}: Este é um dicionário com uma única chave vazia ('') e um 
# valor que é i + 1. O i + 1 é usado para criar os índices das linhas, 
# começando de 1 (pois enumerate começa a contar do zero).

# **row: Esta é a parte interessante do código. row é o dicionário original
# de cada item em carta_vinho. O operador ** é usado para desempacotar esse
# dicionário e incluir todas as suas chaves e valores no novo dicionário que
# estamos criando.

# Resumindo, a expressão {**{'': i + 1}, **row} cria um novo dicionário para 
# cada elemento row em carta_vinho, adicionando um índice iniciando em 1 como
# a primeira chave do dicionário. Isso é feito para modificar a estrutura de
# carta_vinho antes de passá-la para a função tabulate, garantindo que cada 
# linha da tabela tenha um índice numérico visível.

print(tabulate.tabulate(carta_vinho, headers= 'keys', tablefmt= 
                        'rounded_grid', showindex= 'num', stralign='center'))