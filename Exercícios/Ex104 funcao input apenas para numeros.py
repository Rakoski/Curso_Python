# Crie um programa que tenha a função leiaint(), que vai funcionar semelhante a função input() do python, só que fazendo
# a validação para aceitar apenas números.

def leiaint(self):
    while True:
        try:
            numero = int(input(self))
        except (ValueError, TypeError):
            print('\033[1;31mPor favor, digite um número inteiro válido\033[m')
            continue
        else:
            return numero


def leiafloat(self):
    while True:
        try:
            numero = float(input(self))
        except (ValueError, ZeroDivisionError, TypeError):
            print('\033[1;31mPor favor, digite um número real válido!\033[m')
            continue
        else:
            return numero


n = leiaint('Digite seu número inteiro: ')
f = leiaFloat('Digite seu número real: ')
print(f'Os números digitados foram {n} e {f}')