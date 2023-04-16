#Aprimore o desafio anterior, mostrando no final: a) a soma de todos valores pares digitados, b) A soma dos valores da terceira coluna
#c) o maior valor da segunda linha
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacoluna3 = 0

for coluna in range(0, 3):
    for linha in range(0, 3):
        matriz[coluna][linha] = int(input(f'Digite seu valor para {coluna}, {linha}:'))

        #if para a soma dos valores pares
        if matriz[coluna][linha] % 2 == 0:
            somapar += matriz[coluna][linha]

#For para a soma da terceira coluna
for coluna in range(0, 3):
    somacoluna3 += matriz[coluna][2]

#max para os valores da segunda linha
maiordaseglinhakk = max(matriz[1])


for coluna in range(0, 3):
    for linha in range(0, 3):
        print(f'[{matriz[coluna][linha]}]', end='')
    print()
print(somapar, somacoluna3, maiordaseglinhakk)
print(f'A soma dos valores pares é {somapar}, a soma dos valores da terceira coluna é {somacoluna3}', end=', ')
print(f'E o maior valor da segunda linha é {maiordaseglinhakk}')