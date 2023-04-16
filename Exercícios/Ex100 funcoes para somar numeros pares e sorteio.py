# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e SomaPar(). A primeira função
# Vai sortear 5 números e vai colocá-los dentro de uma lista, já a segunda função vai mostrar a soma entre todos os va-
# lores PARES sorteados pela função anterior
from random import randint
from time import sleep


def sorteia(lista):
    for cont in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto! ')


def somapar(lista):
    soma = 0
    par = []
    for every in lista:
        if every % 2 == 0:
            soma += every
            par.append(every)
    print(f'Somando os valores de {lista} temos {soma}, pois os valores {par} são pares')



#programa principal
numeros = []
sorteia(numeros)
somapar(numeros)
