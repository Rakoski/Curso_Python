#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e
#também indique o menor e o maior valor que estão na tupla
from random import randint
tupla = randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5)
print(f'{tupla}')
print(f'Seu maior valor é {max(tupla)}')
print(f'Seu menor valor é {min(tupla)}')


