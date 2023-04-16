#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado, no final, mostre a matriz na tela, com a
#formatação correta

#----------------------------------------------------------------------------------------------------------------------
#esse foi o jeito que eu fiz, que deu certo, mas vou colocar o jeito que ele fez também
#a01 = []
#b01 = []
#c01 = []
#a02 = []
#b02 = []
#c02 = []
#a03 = []
#b03 = []
#c03 = []
#a01.append(int(input('Digite seu valor para 3, 1: ')))
#a02.append(int(input('Digite seu valor para 3, 2: ')))
#a03.append(int(input('Digite seu valor para 3, 3: ')))
#b01.append(int(input('Digite seu valor para 2, 1: ')))
#b02.append(int(input('Digite seu valor para 2, 2: ')))
#b03.append(int(input('Digite seu valor para 2, 3: ')))
#c01.append(int(input('Digite seu valor para 3, 1: ')))
#c02.append(int(input('Digite seu valor para 3, 2: ')))
#c03.append(int(input('Digite seu valor para 3, 3: ')))
#print(a01, a02, a03)
#print(b01, b02, b03)
#print(c01, c02, c03)
#----------------------------------------------------------------------------------------------------------------------
#jeito que ele resolveu

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for coluna in range(0, 3):
    for linha in range(0, 3):
        matriz[coluna][linha] = int(input(f'Digite seu valor para {coluna}, {linha}:'))


for coluna in range(0, 3):
    for linha in range(0, 3):
        print(f'[{matriz[coluna][linha]}]', end='')
    print()








