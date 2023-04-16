#Aprimore o desafio 95 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de
#cada jogador
fifa = dict()
pes = list()
time = list()
while True:
    fifa.clear()
    fifa['nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas o {fifa["nome"]} jogou? '))
    pes.clear()
    for cont in range(0, partidas):
        pes.append(int(input(f'Quantos gols ele fez na partida {cont + 1}? ')))
    fifa['gols'] = pes[:]
    fifa['partidas'] = partidas
    soma = sum(pes)
    time.append(fifa.copy())
    while True:
        pergunta = str(input('Deseja continuar? [sim/não]: ')).strip().lower()
        if pergunta in 'simnão': #é um while dentro de outro while, justamente para a pessoa não ter erros em digitar
            #algo diferente de sim ou não
            break
        print('Erro! Digite sim ou não')
    if pergunta == 'não':
        break

#A partir dessa parte são vários loops for justamente para fazer um menu bonitin com todos os dados dos jogadores
#e dos gols e partidas deles.
print('-' * 40)
print('cod ', end='')
for elementos in fifa.keys():
    print(f'{elementos:<15}', end='')
print()
print('-' * 40)
for keys, values in enumerate(time):
    print(f'{keys + 1:>3} ', end='')
    for dados in values.values():
        print(f'{str(dados):<15}', end='')
    print()

#Não satisfeitos apenas com aquilo, isso aqui mostra cada jogador individualmente, levantando seus dados de 1 em um
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para): '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Esse jogador não existe!')
    else:
        print(f' Levantamento do jogador {time[busca]["nome"]}:')
        for i, gols in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+ 1}, fez {gols} gols')
    print('-' * 40)
print('Obrigado por usar!')