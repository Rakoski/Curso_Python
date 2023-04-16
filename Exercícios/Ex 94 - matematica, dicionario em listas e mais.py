#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os
#dicionários em uma lista. No final mostre: a) Quantas pessoas foram cadastradas, b) A média de idade do grupo, c) Uma lista com todas
#as mulheres, d) uma lista com todas as pessoas de idade acima da média.
pessoas = dict()
idade = dict()
mulheres = list()
cont = soma = 0
lista = list()
listadaspessoasmaiorqamedia = list()
while True:
    pessoas.clear() #Lembrando que esse clear é necessárissimo para q n vire bagunça tanto nas listas quanto nos dicionarios
    pessoas["nome"] = str(input('Digite seu nome: '))
    #Esse loop while é para descobrirmos o sexo, sendo q se eu nn digitar "M" ou "F", ele faz vc falar dnv
    while True:
        pessoas["sexo"] = str(input('Digite seu sexo: ')).upper().strip()
        if pessoas["sexo"] not in 'MF': #esse é somente para sabermos se é M ou F, se não for, volta à pergunta
            print('Digite um sexo válido! ')
        if pessoas["sexo"] in 'F':
            mulheres.append(pessoas["nome"]) #Se for mulher é colocada na lista "mulheres"
            break
        elif pessoas["sexo"] in 'M':
            break
    #Essa parte é sobre a idade, sendo perguntada ela
    pessoas["idade"] = int(input('Digite sua idade: '))
    lista.append(pessoas.copy()) #Coloca-se a idade dentro da lista
    soma += pessoas["idade"] #soma todas as idades colocadas no dicionário
    cont += 1 #contador para sabermos quantas pessoas foram adicionadas e para a média
    media = soma / cont #média estabelecida
    if pessoas["idade"] >= media:
        listadaspessoasmaiorqamedia.append(pessoas["nome"]) #coloca todas as pessoas com idade maior que a média
                                                            #dentro dessa lista
    #esse código é apenas para nos mostrar se a pessoa quer continuar ou não, com um erro se ela colocar algo diferente
    #de sim ou não
    while True:
        pergunta = str(input('Deseja continuar? [sim/não]: ')).strip().lower()
        if pergunta in 'simnão': #é um while dentro de outro while, justamente para a pessoa não ter erros em digitar
            #algo diferente de sim ou não
            break
        print('Erro! Digite sim ou não')
    if pergunta == 'não':
        break
print('-=' * 30)
print(f'Foram cadastradas {cont} pessoas')
print(f'As mulheres são {mulheres}')
print(f'A média é de {media}')
print(f'Temos que {listadaspessoasmaiorqamedia} tem sua idade maior que {media}')