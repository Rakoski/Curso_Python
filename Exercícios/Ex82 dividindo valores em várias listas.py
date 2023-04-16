#Crie uma lista que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter os números
#pares e os valores ímpares digitados respectivamente. Ao final, mostre o conteúdo das 3 listas geradas.
numeros = list()
a = list()
b = list()
pergunta = 'sim'
while pergunta == 'sim':
    n = int(input("Digite um número: "))
    numeros.append(n)
    if n % 2 == 0:
        a.append(n)
    else:
        b.append(n)
    pergunta = str(input('Quer continuar? [sim/não]: ')).strip().lower()
numeros.sort()
a.sort()
b.sort()
print(f"Seus valores {numeros} pares são {a} e os ímpares são {b}")


