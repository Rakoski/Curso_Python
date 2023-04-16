# Faça um programa que tenha uma função chamada contador() que receba três parâmetros: início, meio e fim e realize a contagem
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1.
# b) de 10 até 0, de 2 em 2.
# c) uma contagem personalizada
from time import sleep
def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += passo
            sleep(0.68)
            if passo > 0:
                cont += passo
                sleep(0.7)
            elif passo < 0:
                passo *= -1
                cont += passo
                sleep(0.6)
            elif passo == 0:
                passo = 1
                cont += 1
                sleep(0.7)
        print('fim! ')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            if passo < 0:
                passo *= -1
                cont -= passo
                sleep(0.7)
            elif passo > 0:
                abs(passo)
                cont -= passo
                sleep(0.7)
            elif passo == 0:
                passo = 1
                cont -= 1
                sleep(0.7)
        print('fim! ')


i = int(input('Digite seu número para o início: '))
f = int(input('Agora digite seu fim: '))
p = int(input('Finalmente, digite seu passo: '))
contador(inicio=i, fim=f, passo=p)
pergunta = str(input('Deseja realizar o contador denovo? [sim/não]: '))