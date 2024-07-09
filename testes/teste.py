def limpa_tela():
    """_summary_
    """
    import os
    os.system('cls')


def soma(a, b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    resultado = a + b
    return resultado


def firula():
    print('-' * 70)
    

#724

limpa_tela()
firula()
resposta = soma(1, 2)
print(f'A soma de 2 números é: {resposta}')
firula()
print()