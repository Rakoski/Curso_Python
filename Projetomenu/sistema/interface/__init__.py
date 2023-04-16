from utilidadescev.moeda import *

def linha(tamanho=42):
    return "-" * 42


def Cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    Cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;32m{c} \033[m- \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Opção: ')
    return opc


