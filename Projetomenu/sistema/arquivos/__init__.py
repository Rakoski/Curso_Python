from Projetomenu.sistema.interface import *
from time import sleep

def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except (FileExistsError, FileNotFoundError):
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso! ')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um Erro!')
    else:
        print(f'Lendo...')
        sleep(0.5)
        Cabecalho('PESSOAS CADASTRADAS')
        for linhas in a:
            dado = linhas.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]}; {dado[1]} anos')


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except (FileNotFoundError, FileExistsError):
        print(f'Arquivo não encontrado!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print(f'Houve um erro na hora de escrever os arquivos!')
        else:
            print(f'\033[1;32m{nome} adicionado(a)\033[m')
            a.close()
