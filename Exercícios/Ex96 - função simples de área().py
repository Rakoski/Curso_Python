# Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e com-
#primento) e mostre a área do terreno
print('Controle de terrenos')
print('-' * 40)


def area(c, l):
    a = l * c
    print(f'A área desse terreno é de {float(a):.2f}m²')


comprimento = float(input('Digite seu comprimento: '))
largura = float(input('Digite sua largura: '))
area(c=comprimento, l=largura)
