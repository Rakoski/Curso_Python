#Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre: a)Quantas vezes apareceu o valor 9
#b) Em que posição foi digitado o primeiro valor 3 e c)Quais foram os números pares:

#Note que para transformarmos um int em uma tupla, é preciso do parenteses antes do (int(input:))
valor = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite algum outro número: ')))
print(f'O número 9 apareceu {valor.count(9)} vezes')
print(f'o número 3 está na {valor.index(3)+1}ª posição')
for n in valor:
    if n % 2 == 0:
        print(n, end= ', ')


