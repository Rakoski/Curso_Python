# Menu com várias opções de manipulação completo!

from Projetomenu.sistema.interface import *
from Projetomenu.sistema.arquivos import *
from utilidadescev import moeda


print(globals())
arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Colocar nova pessoa', 'Sair do programa'])

    # Opção de ler os arquivos que eu já tenho
    if resposta == 1:
        lerArquivo(arq)

    # Opção de cadastrar uma nova pessoa
    elif resposta == 2:
        Cabecalho('NOVO CADASTRO')
        nome = leiaStrip('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arquivo=arq, nome=nome, idade=idade)

    # Opção de dar break no loop e sair do programa
    elif resposta == 3:
        print('Obrigado por utilizar o programa!')
        break
    else:
        print('\033[1;31mErro, digite uma opção válida\033[m')
