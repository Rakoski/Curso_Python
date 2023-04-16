#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 1) Quantas pessoas foram
#cadastradas 2) Uma listagem com as pessoas mais pesadas 3) Uma listagem com as pessoas mais leves
galera = []
pessoas = []
maior = menor = 0

#Esse código serve pra ver qual é o maior e menor peso de todas as pessoas digitadas, enquanto a pessoa digita "sim" para a pergunta
while True:
    galera.append(str(input('Digite seu nome: ')))
    galera.append(float(input('Digite seu peso: ')))

#Essa é uma das partes mais importantes, pois é mostrado como vemos as maiores e menores pessoas
    #Dentro de uma lista complexa
    if len(pessoas) == 0:
        maior = menor = galera[1]
    else:
        if galera[1] > maior:
            maior = galera[1]
        elif galera[1] < menor:
            menor = galera[1]

    pessoas.append(galera[:])
    galera.clear()
    pergunta = str(input('Deseja continuar? [sim/não]: '))
    if pergunta == 'não':
        break

#Aqui só registra quantas pessoas ela colocou
print()
print(f'Você cadastrou {len(pessoas)} pessoas')

#Essa é a parte mais importante, porque vê quem tem o maior peso, sendo dados os valores anteriores
for valor in pessoas:
    if valor[1] == maior:
        print(f'O maior peso é de {valor[0]}, com {maior}kg')
    elif valor[1] == menor:
        print(f'O menor peso é de {valor[0]}, com {menor}kg')


