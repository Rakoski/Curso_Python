# Faça um mini-sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai aparecer
# Quando o usuário digitar a palavra FIM o programa se encerrará. Obs: use cores
def ajuda(com):
    print(f'\033[1;33m')
    help(com)
    print(f'\033[m')


def titulo(mensagem):
    tamanho = len(mensagem)
    print('\033[1;32m-' * (tamanho + 5))
    print(f'  {mensagem:<2}')
    print('\033[1;32m-\033[m' * (tamanho + 5 ))

while True:
    titulo('PROGRAMA DE AJUDA EM PYTHON')
    comando = str(input('Digite seu comando: '))
    if comando == 'FIM' or comando == 'fim':
        print('Obrigado por usar!')
        break
    else:
        ajuda(comando)
