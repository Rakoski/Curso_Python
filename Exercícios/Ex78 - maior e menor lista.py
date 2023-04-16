#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado
#e a respectiva posição na lista
valores = []
maior = 0
menor = 0
x = 0
cont = 0


#Mecanismo pra ver qual é o maior ou menor
#Lembrando que também existem os comandos max(valores) e min(valores)
for cont in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {cont + 1}: ")))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        elif valores[cont] < menor:
            menor = valores[cont]


#Printe maior valor e sua posição
print(f"A lista é {valores}")
print(f"O maior valor é {maior}, na posição ", end='')
for indice, valor in enumerate(valores):  #Esse loop serve pra falar a posição que está o número maior, perceba o comando enumerate
    if valor == maior:
        print(f"{indice + 1}", end=', ')


#Já esse é pra printar o menor valor e sua posição
print()
print(f"O menor valor é {menor}, na posição ", end='')
for indice, valor in enumerate(valores):  #Esse faz a mesma coisa, mas pro menor número
    if valor == menor:
        print(f"{indice + 1}", end=', ')

