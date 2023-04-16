from time import sleep

def contador(inicio, fim, passo):
    """
    => Establishes a number counting system with a beginning, end and rhythm.
    :param inicio = Which number does it starts with?
    :param fim =  Which number does it end with?
    :param passo =  What is the rhythm of the counting? Is it from 2 to 2, for example?
    :return: sem retorno
    Made my Mateus Rakoski
    """""

    c = inicio
    while c <= fim:
        print(f'{c} ', end='', flush=True)
        sleep(0.24)
        c += passo
    print('Fim!')


#contador(2, 10, 2)
#help(contador)


def fatorial(num = 1 ): # aka caso eu não informe número ele vai ser 1
    f = 1
    for cont in range(num, 0, -1):
        f *= cont
    return f


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
