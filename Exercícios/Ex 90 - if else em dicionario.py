#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estru
#tura na tela
aluno = dict()
aluno['nome'] = str(input('Digite seu nome: '))
media = float(input(f'digite a média de {aluno["nome"]}: '))
if media >= 6:
    print(f'A situação de {aluno["nome"]} é de aprovado(a)')
else:
    print(f'A situação de {aluno["nome"]} é de reprovação')