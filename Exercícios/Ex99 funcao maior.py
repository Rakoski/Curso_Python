# Faça uma função chamada maior(), que receba vários parâmetros inteiros. Seu programa tem que analisar todos os valores
# e dizer qual é o maior
from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo. ')
    print(f'O maior valor informado foi {maior}')


maior(9, 5, 4, 2, 7)
maior(4, 3, 2, 1, 7)