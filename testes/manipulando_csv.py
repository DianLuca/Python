import csv
import os

pasta = 'testes/arquivo_csv/'

# Caminho do arquivo
arquivo = 'testes/arquivo_csv/manipulacao.csv'

caminho = os.path.join(pasta, arquivo)

cadastro = []

registro = {}

# A intenção é criar um arquivo e se iniciar novamente os dados contindos 
# nele não sejam alterados
os.makedirs(pasta, exist_ok=True)

if arquivo:
    with open(arquivo, 'w', newline='') as arquivo_csv:
        campos = ['nome', 'idade']
            
        escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
        
        escrever.writeheader()
        
        arquivo_csv.truncate()
        
while True:


    os.system('cls')
    menu = input('1 - Cadastro | 0 - Sair: ')
    while menu == '1':
        
        nome = input('Insira seu nome: ')
        idade = input('Insira sua idade: ')
        registro['nome'] = nome
        registro['idade'] = idade
        cadastro.append(registro.copy())
        with open(arquivo, mode='a', newline='', encoding='utf-8') as arquivo_csv:
            
            campos = ['nome', 'idade']
            escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
            
            # escrever.writeheader()
            escrever.writerows(cadastro)
        input(cadastro)
        # Cadastrando um arquivo
        break
    if menu == '0':
        print('Programa Encerrado!')
        break
    


# Abrindo o arquivo em modo "w+"
    # # Criando um objeto reader para ler o CSV
    # reader = csv.reader(arquico_csv)
    
    # # Lendo o conteúdo do arquivo e armazenando na memória
    # linhas = list(reader)
    
    # # Criando um objeto writer para reescrever o CSV com os dados modificados
    # escrever.writeheader()
    # escrever.writerows(cadastro)
    
    # # Truncando o arquivo para remover qualquer dado extra que permaneceu

print("Alteração realizada com sucesso!")
