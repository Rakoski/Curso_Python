#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se
#por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente
#além da idade, com quantos anos a pessoa vai se aposentar (35 anos de contribuição)
from datetime import datetime
dicionario = dict()

dicionario['nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
dicionario['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
dicionario['idade'] = datetime.now().year - nasc

if dicionario['ctps'] != 0:
    dicionario['contratação'] = int(input('Ano de contratação: '))
    dicionario['Salário'] = int(input('Salário: '))
    dicionario['aposentadoria'] = dicionario['idade'] + ((dicionario['contratação'] + 35) - datetime.now().year)

print()
print('-=' * 30)
print()


print(f'Seu nome é {dicionario["nome"]}')
print(f'Você nasceu em {nasc}')
print(f'Sua carteira de trabalho é {dicionario["ctps"]}')
print(f'Você possui R${dicionario["Salário"]} de salário')
print(f'E sua aposentadoria será com {dicionario["aposentadoria"]} anos')





