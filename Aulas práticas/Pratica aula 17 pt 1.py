lista = [1, 2, 5, 9, 40, 2]
print(f"A lista tem {len(lista)} números e é {lista} antes de tudo")

lista[2] = 1
print(f"a lista tem {len(lista)} números e é {lista} depois de colocar o 1 no 2º lugar")

lista.append(3)
lista.sort()
print(f"a lista tem {len(lista)} números e é {lista} após ser sortada e colocado o 3")

lista.pop(2)
print(f"A lista tem {len(lista)} números e é {lista} após serem popados os 2")

lista.sort(reverse=True)
print(f"A lista tem {len(lista)} números e é {lista} após ser revertida")