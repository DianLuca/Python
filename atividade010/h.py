# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 12/07/2024

# Uma Academia deseja fazer uma pesquisa entre seus clientes para descobrir a
# média de altura  e peso de seus clientes. Faça um programa que pergunte a
# cada um dos clientes da academia seu código, nome, altura e peso. Após esse
# cadastramento, seu programa deverá listar os dados dos clientes e a média.
# Para sair do programa o usuário deverá digitar o valor zero(0). O número de
# clientes é indefinido. Veja a saída no próximo slide.
import os


os.system('cls')

clientes = []
cliente = {}


def cadastro(**info):
    cliente = info
    clientes.append(cliente.copy())


def media_peso_altura():
    media_altura, media_peso = 0, 0
    soma_altura, soma_peso = 0, 0
    if len(clientes) == 0:
        print('Não existem clientes para fazer a média!')
    else:
        for aluno in clientes:
            soma_altura += float(aluno['altura'])
            soma_peso += float(aluno['peso'])
            media_altura = soma_altura / len(clientes)
            media_peso = soma_peso / len(clientes)
    return media_altura, media_peso


def exibir_alunos():
    if len(clientes) == 0:
        print('Não há nenhum aluno cadastrado!')
    else:
        for aluno in clientes:
            for k, v in aluno.items():
                print(f'{k}: {v}', end=' | ')
            print()


while True:
    print('|--- ACADEMIA ---|')
    menu = input('1 - Cadastrar | 2 - Média de Peso e Altura | '
                 '3 - Exibir Lista de Aluno(s) | 0 - Sair : ')
    os.system('cls')
    if menu == '1':
        while True:
            print('MENU DE CADASTRO')
            # codigo = input('Insira o seu código: ').strip()
            nome = input('Insira o seu nome: ').title().strip()
            altura = input('Insira o sua altura: ').strip().replace(',', '.')
            peso = input('Insira o seu peso: ').strip().replace(',', '.')
            cadastro(codigo=len(clientes)+1, nome=nome, altura=altura, peso=peso)
            os.system('cls')
            break
    elif menu == '2':
        altura_media, peso_media = media_peso_altura()
        print(f'A academia tem {len(clientes)} aluno(s) e a média de peso e '
              + 'altura geral da academia: ')
        print(f'Peso: {peso_media:.2f} Kg.')
        print(f'Altura: {altura_media:.2f} m.')
        input('Para voltar ao menu pressione ENTER: ')
        os.system('cls')
    elif menu == '3':
        print('|--- LISTA DE ALUNOS ---|')
        exibir_alunos()
        print()
        input('Para voltar ao menu pressione ENTER: ')
        os.system('cls')
    elif menu == '0':
        break
    else:
        print('Opção inválida!')
