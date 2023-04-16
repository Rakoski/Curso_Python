from math import sqrt


def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def leiadinheiro(self):
    valido = False
    while not valido:
        entrada = str(input(self)).replace(',', '.').strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'{entrada} é um preço inválido!')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mNúmero inválido, digite novamente\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[1;31mUsuário escolheu não digitar\033[m')
            return 0
        else:
            return n


def leiaStrip(msg):
    while True:
        n = str(input(msg)).strip()
        if not n.isalpha():
            print(f'\033[1;31mDigite uma frase válida!\033[m')
        else:
            return n


def dobro(n, formato=False):
    return n * 2 if formato is False else moeda(n)


def triplo(n, formato=False):
    return n * 3 if formato is False else moeda(n)


def bhaskara():
    while True:
        try:
            a = int(input('a: '))
            b = int(input('b: '))
            c = int(input('c: '))
            delta = b*b - 4*a*c
            if delta < 0:
                print(f'Seu delta não tem raízes reais, digite novamente')
                continue
            elif delta == 0:
                x = -b / (2*a)
                print(f'Temos duas soluções iguais no valor de {x:.2f}')
                continue
            elif delta > 0:
                x1 = (-b + sqrt(delta)) / (2*a)
                x2 = (-b - sqrt(delta)) / (2*a)
                print(f'Temos como duas soluções possíveis o x1 = {x1:.2f} e o x2 como {x2:.2f}')
                break
        except (ValueError, TypeError):
            print(f'Valores pulados, digite novamente')
            continue


# Ex107:
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir() e metade(). Faça também um
# programa que use algumas dessas funções e use algumas delas.


def aumentar(numero, porcentagem=10, formato=False):
    aumentofinal = numero + (numero * (porcentagem / 100))
    return aumentofinal if formato is False else moeda(numero)


def diminuir(numero, porcentagem=10, formato=False):
    diminuirfinal = numero - (numero * (porcentagem / 100))
    return diminuirfinal if formato is False else moeda(numero)


def metade(numero, formato=False):
    return numero / 2 if formato is False else moeda(numero)


# Ex108:
# Adapte o código do ex107, criando uma função chamda moeda() que mostre os valores como um valor monetário formatado


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


# Ex110:
# Adicione ao módulo moeda.py criado nos desafios anteriores uma função chamada resumo() que mostre algumas informações
# que já temos no módulo até aqui

def resumo(numero, porcentagem):
    print('-' * 30)
    print(f'  Preço analisado: R${numero}')
    print(f'-' * 30)
    diminuirfinal = numero - (numero * (porcentagem / 100))
    print(f'Seu número diminuido em {porcentagem}% fica R${diminuirfinal}')
    aumentofinal = numero + (numero * (porcentagem / 100))
    print(f'Seu número aumentado em {porcentagem}% fica R${aumentofinal}')
    print(f'A metade de seu número é R${numero / 2}')
    print(f'O seu numero dobrado fica R${numero * 2}')
    print(f'O seu numero triplicado fica R${numero * 3}')