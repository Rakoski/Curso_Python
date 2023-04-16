#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
#partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
#dicionário, incluindo o total de gols feitos durante o campeonato.
fifa = dict()
pes = list()
fifa['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas o {fifa["nome"]} jogou? '))


for cont in range(0, partidas):
    pes.append(int(input(f'Quantos gols ele fez na partida {cont + 1}? ')))

fifa['gols'] = pes #pes é o nome da lista que botei no dicionário
fifa['part idas'] = partidas #partidas é a variável de quantas partidas jogou, só coloquei no dicionário

print('-=' * 30)
print(fifa)

print('-=' * 30)
print(f'{fifa["nome"]} marcou {fifa["gols"]} gols em {fifa["partidas"]} partidas')
print('-=' * 30)

for indice, valor in enumerate(fifa["gols"]):
    print(f' => Na partida {indice + 1} ele marcou um total de {valor} gols')
print(f'{fifa["nome"]} marcou um total de {sum(pes)} gols')