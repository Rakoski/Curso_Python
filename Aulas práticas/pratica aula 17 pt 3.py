pessoas = list()
galera = list()
cont = 0

while cont != 3:
    galera.append(str(input('Digite seu nome: ')))
    galera.append(int(input('Digite sua idade: ')))
    pessoas.append(galera[:])
    galera.clear()
    cont += 1

for p in pessoas:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade pois tem {p[1]} anos', end=', ')
    elif p[1] < 18:
        print(f'{p[0]} é menor de idade pois tem {p[1]} anos', end=', ')
