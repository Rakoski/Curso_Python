#Crie um programa onde 4 jogadores joguem um dado e tenham resultandos aleatórios. Guarde esses resultados em um dicionário
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado
from random import randint
from time import sleep
c = 1
lista = list()

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6),
}

ranking = dict()
for keys, values in jogo.items():
    print(f'O {keys} tirou {values} no dado')
    sleep(1)

#O guanabara fez essa parte diferente, importando do operator o comando itemgetter, mas nessa versão do python
#da pra fazer com só comandos bultins
ranking = dict(sorted(jogo.items(), key=lambda item: item[1], reverse=True))
print(ranking)
for k, v in ranking.items():
    print(f' {c}° lugar: {k} tirou {v} no dado', end=' //')
    c += 1