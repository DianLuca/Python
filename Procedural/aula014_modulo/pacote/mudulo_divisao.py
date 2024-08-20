def dividir(a, b):
    if b == 0:
        return None, 'Erro na divisão'
    else:
        divisao = a / b
        return divisao, 'Ok!'