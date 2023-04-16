#Crie um programa onde o usuário possa digitar 7 valores númericos e cadastre-os em uma lista única que mantenha separados os valores
#os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente
par = list()
impar = list()
listunc = [[], []]

for valor in range(1, 8):
    numero = int(input('Digite seu número: '))
    if numero % 2 == 0:
        listunc[0].append(numero)
    elif numero % 2 != 0:
        listunc[1].append(numero)

listunc[0].sort()
listunc[1].sort()
print()

print(f'Lista par: {listunc[0]}')
print(f'Lista ímpar: {listunc[1]}')
