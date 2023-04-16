#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
#de inserção (sem usar o sort()). No final mostre a lista ordenada na tela:

valores = list()

#Nós vamos ter 3 possibilidades:
#Ou o número é o primeiro, aí já inclui ele de qualquer jeito
#Ou ele é o último //aka o maior, tbm já inclui ele
#Ou ele ta no meio, essa parte que eu não consegui fazer no meu outro código

for c in range(0, 5):
     n = int(input(f'Digite um número: '))
     if c == 0 or n > valores[-1]: #Se esse for o primeiro número da lista ou Se o número for maior do que o último elemento, já pode colocar ele
         if c != 0 and n == valores[-1]:
             print("Valor já adicionado na lista")
         else:
            valores.append(n)
            print("Adicionado no final da lista")


     else: #Essa é a parte difícil do código, a parte do "meio" da lista
        pos = 0
        while pos < len(valores): #Vai da posição 0 até a última posição "checando" cada um dos elementos da lista pra ver se é menor ou não
            if n == valores[pos]: #Se ele for igual, não adicione
                print(f"Valor já adicionado na posição {pos}") #Aqui é só um check pra caso o número já esteja na lista, ele não ser adicionado 2 vezes
                break

            elif n < valores[pos]: #se o n é menor do que o número em que ele ta "checando" pra ele ficar antes
                valores.insert(pos, n) #Assim, se o n for menor, ele já vai colocar na posição anterior a qual ele achou um número maior que ele
                print(f"Adicionado na posição {pos}")
                break
            pos += 1 #Daqui ele já vai pra próxima posição dentro do código //aka volta o loop

print(f"Os valores digitados foram {valores}")
