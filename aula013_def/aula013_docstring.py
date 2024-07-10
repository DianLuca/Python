def limpa_tela():
    """Realizando a limpeza da tela
    """
    import os
    os.system('cls')


def soma(a, b):
    """Realizando soma

    Args:
        a (int): primeiro valor inteiro para somar.
        b (int): segundo valor inteiro para somar.

    Returns:
        int: resultado da soma dos valores da variávies a e b.
    """
    resultado = a + b
    return resultado


def firula():
    """Saída para formatação no terminal
    """    
    print('-' * 70)
    

#724

limpa_tela()
firula()
resposta = soma(1, 2)
print(f'A soma de 2 números é: {resposta}')
firula()
print()