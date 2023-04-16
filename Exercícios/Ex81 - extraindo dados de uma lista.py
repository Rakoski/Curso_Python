#Crie uma lista que vai ler vários números e colocar em uma lista. Depois disso, mostre: a) quantos números foram digitados. b) A lista
#de valores ordenada de forma decrescente. c) Se o valor 5 foi digitado e está ou não na lista.
numeros = list()

while True:
    numeros.append(int(input("Digite seu numero: ")))

    pergunta = str(input('Quer continuar? [sim/não]: '))
    if pergunta != 'sim':
        break

print(f'Foram digitados {len(numeros)} números')
numeros.sort(reverse=True)
print(f"Os números em ordem decrescente são {numeros}")
if 5 in numeros:
    print(f"O número 5 está na lista")
else:
    print(f"O número 5 não está na lista")