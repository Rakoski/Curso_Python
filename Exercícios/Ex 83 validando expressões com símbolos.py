#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada
#está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite sua expressão: '))
pilha = list()

for simb in expressao:
    if simb == '(':
        pilha.append('(')

    elif simb == ')': #O comando funciona removendo cada "par" de parenteses que ele encontra
        if len(pilha) > 0: #Ou seja, se ele  encontrar um parenteses fechado,
            pilha.pop() #Ele remove ele

        else: #Esse é o caso de ele não encontrar parênteses fechado
            # ou encontrar um fechado sem ter aberto nada, ai ele da break e um erro ocorre
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Erro!')
