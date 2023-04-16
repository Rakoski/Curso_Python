# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e o segundo chamado show que será um valor lógico (opcional) indicando se será mostrado ou não na tela run
def fatorial(num=1, show=False):

    """Shows the factorial of a number
    :param num: not optional. Inserts the number to be factored
    :param show: optional. If true, shows the math to get to said number
    Made by Mateus"""

    f = 1
    for c in range(num, 0, -1):
        # Se o show=True, isso vai acontecer:
        if show:
            if c > 1:
                print(f'{c} * ', end='')
            else:
                print(f'{c} = ', end='')
                # Esse código mostra a conta do fatorial, sendo que se o contador for menor que 1
                # ele já mostra como igual. EX: 5 x 4 x 3 x 2 x 1 = 120

        # Faz com que 1 seja multiplicado {c} vezes, assim sendo fatorado
        f *= c
    return f
    # Retorna o f para poder fazer tal código quantas vezes quisermos


print(fatorial(5, show=False))
help(fatorial)
