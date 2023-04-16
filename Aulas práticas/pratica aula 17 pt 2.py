#Isso é mais sobre como usar o for em uma lista, não sei ainda sobre o while

valores = list() #Esse comando é a mesma coisa que colocar [chaves], serve pra criar uma lista
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: '))) #Comando simples pra criar uma lista de input com 5 números

for v in valores:  #Isto é, pra cada valor da minha lista
    print(f"{v}", end=', ')  #Printe todos os valores da lista, sendo que antes do loop voltar pra printar o próximo número
                              #coloque uma vígula antes de acabar esse loop

for p, v in enumerate(valores): #O p é a posição e o v é o próprio valor dos valores
                                #É preciso lembrar que também tem que se enumerar os valores, já que eles são parte de um
                                #Objeto [lista] e não [int], é exatamente pra isso que o enumerate serve
    print(f"Na posição {p + 1}, encontrei o valor {v}")
print("Final da lista")
