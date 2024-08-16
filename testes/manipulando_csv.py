import csv
import os

cadastro = [
    {'nome':'Bob','idade': '25','cidade':'Juiz de Fora'}
]
pasta = 'testes/arquivo_csv/'
os.makedirs(pasta, exist_ok=True)
# Caminho do arquivo
arquivo = 'testes/arquivo_csv/manipulacao.csv'

caminho = os.path.join(pasta, arquivo)
# Abrindo o arquivo em modo "w+"
with open(arquivo, mode='w+', newline='', encoding='utf-8') as file:
    
    campos = ['nome', 'idade', 'cidade']
    
    escrever = csv.DictWriter(file, fieldnames=campos, delimiter=';')
    
    escrever.writeheader()
    escrever.writerows(cadastro)
    # Criando um objeto reader para ler o CSV
    reader = csv.reader(file)
    
    # Lendo o conteúdo do arquivo e armazenando na memória
    linhas = list(reader)
    
    # Modificando o dado desejado
    for linha in cadastro:
        if linha['nome'] == 'Bob':  # Verifica se a primeira coluna (Nome) é 'Bob'
            linha['idade'] = '26'  # Altera a idade (segunda coluna)
    
    # Movendo o cursor para o início do arquivo para sobrescrever
    file.seek(0)
    
    # Criando um objeto writer para reescrever o CSV com os dados modificados
    escrever.writeheader()
    escrever.writerows(cadastro)
    
    # Truncando o arquivo para remover qualquer dado extra que permaneceu
    file.truncate()

print("Alteração realizada com sucesso!")
