import os


os.system('cls')
# Lista de dicionários
estoque = [
    {"produto": "Camiseta", "quantidade": 50, "preco_unitario": 25.99},
    {"produto": "Calça", "quantidade": 30, "preco_unitario": 39.99},
    {"produto": "Blusa", "quantidade": 20, "preco_unitario": 19.99},
    {"produto": "Calça Jeans", "quantidade": 30, "preco_unitario": 39.99},
    {"produto": "Alça Jeans", "quantidade": 30, "preco_unitario": 39.99}
]

busca = input('Busca: ').strip()
itens = 0

encontrado = False  # Variável para controlar se o item foi encontrado

# Verifica se os valores associados à chave "produto" começam com o prefixo especificado
for item in estoque:
    if busca.lower() in item["produto"].lower():  # Usamos lower() para tornar a comparação insensível a maiúsculas e minúsculas
        print(f'Nome do produto: {item["produto"]} | Quantidade: {item["quantidade"]} | Valor: {item["preco_unitario"]}')
        encontrado = True

if not encontrado:
    print('Nenhum item encontrado com essa palavra nos nomes dos produtos.')
