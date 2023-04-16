#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear
#6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep

lista = []
jogos = list()

print('-' * 30)
print('JOGADOR DA MEGA SENA')
print('-' * 30)
x = int(input('Quantos jogos quer que eu sorteie? '))
tot = 1

while tot <= x:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('-=-'* 3, f'\033[1;32mSORTEANDO {x} JOGOS', '\033[m-=-'* 3)
for indice, lista in enumerate(jogos):
    print(f'jogo {indice + 1}: {lista}')
    sleep(1)
print('-=-' * 3, f'\033[1;32mJOGOS SORTEADOS', '\033[m-=-'* 3)