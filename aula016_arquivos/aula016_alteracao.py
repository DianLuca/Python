import csv
import os


os.system('cls')

arquivo = 'aula016_arquivos/arquivos_csv/gravacao/alunas.csv'

nome_para_alterar = input('Qual nome deseja alterar: ')

novo_nome = input('Insira o novo nome: ')
novo_telefone = input('Insira o novo telefone: ')
novo_cidade = input('Insira o novo cidade: ')


alterado = False

# Lendo o arquivo para buscar o que será alterado
with open(arquivo, 'r') as arquivo_csv:
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    cadastro = list(leitura)
    
    for registro in cadastro:
        if registro['nome'] == nome_para_alterar:
            if novo_nome:
                registro['nome'] = novo_nome
            if novo_telefone:
                registro['telefone'] = novo_telefone
            if novo_cidade:
                registro['cidade'] = novo_cidade
            alterado = True

# Realizando a alteração do item
if alterado:
    with open(arquivo, 'w', newline='') as arquivo_csv:
        campos = ['nome', 'telefone', 'cidade']
        escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
        
        escrever.writeheader()
        escrever.writerows(cadastro)
        print('Alterado com sucesso!')
else:
        print('Erro!')
        