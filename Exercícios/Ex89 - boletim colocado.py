#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo
#a média de cada um e permita que o usuário possa mostrar as notas de cada usuário individualmente
from time import sleep
ficha = list()

#Aqui é onde formamos o cadastro, tanto do nome do aluno, notas e média
while True:
    nome = str(input('Digite seu nome: '))
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media]) #Assim, tudo é incorporado na ficha
    #o nome é ficha[0], as notas são ficha[1] e a média ficha[2]
    resposta = str(input('Quer continuar? [sim/não]: ')).strip().lower()
    if resposta != 'sim':
        break

print('-=' * 30)
print(f'{"No.":<4}'
      f'{"NOME":<10}'
      f'{"MÉDIA":>8}')
print('-' * 26)

#Aqui é o boletim propriamente dito
#Com o enumerate() para a contagem de cada aluno e seu nome {aluno[0]} e sua média {aluno[2]}
#Sendo o aluno, a própria variável dita, enquanto o índice é só a contagem de qual aluno é, para ser usado o enumerate()
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}' #aka coloque a contagem de quantos alunos tem 4 casas para a direita
          f'{aluno[0]:<10}' #aka coloque o aluno[0] (nome do aluno) 10 casas para a direita
          f'{aluno[2]:>8.1f}') #aka coloque o aluno[2] (média do aluno) 10 casas para a esquerda e coloque como decimal
print()

#Aqui acessa cada usuário individualmente
while True:
    opcao = int(input('Qual aluno você quer ver as notas? (999 finaliza): '))
    if opcao == 999:
        break
    if opcao <= len(ficha) - 1: #O aluno escolido tem que ser menor do que a quantidade de alunos cadastrados
        #lembrando que o len() ao contrário de outras contagens, começa no 1, assim precisamos colocar ele como -1
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
        #Vulgo as notas de "tal" aluno são "notas 1 e 2 deste aluno escolido anteriormente na variável opcao"

        if media >= 6:
            print(f'Esse aluno passou, pois sua média é {media:.2f}')
        elif media < 6:
            print(f'Esse aluno ficou de recuperação, pois sua média é {media:.2f}')
    print()

print('Finalizando...')
sleep(1)
