#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá
#dentro, ele não será adicionado. No final, serão adicionados todos os valores únicos digitados, em ordem crescente.
valoresnum = list()
resposta = 'sim'

#Essa parte é o coração do código, aqui ta toda a parte da lista, principalmente a parte do 'if n not in lista'
while resposta == 'sim':
    n = int(input('Digite outro valor: '))
    if n not in valoresnum:
        valoresnum.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, não é possível adicionar')

#Aqui no caso eu coloquei a parte pra repetir o loop, se ele disser algo diferente de sim, o loop para
    resposta = str(input('Quer continuar? [sim/não]: '))
    if resposta != 'sim':
        break


valoresnum.sort()
print(f"Os números digitados em ordem crescente são {valoresnum}")
