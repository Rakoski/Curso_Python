#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. No final, mostre uma listagem de preços
#organizando os dados de forma tabular

#Listagem da tupla
produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)


#formatação central dos '=' pra ficar mais bonito
print("="*50)
#Lembrando que esse {:^50} significa centralizado em 50, pra ficar mais bonito
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)

#Loop pra dividir os produtos, começando em 0, até o lenght da tupla, pulando de dois em dois
for c in range(0, len(produtos), 2):
    #Printe os produtos, pulando de dois em dois (assim só printando os produtos), sendo que printe também os números dos produtos
    #pulando de 2 em 2, dessa vez começando no 1 (que é o preço do lápis na tupla)
    print(f"{produtos[c]:.<40}", f" R${produtos[c+ 1]:>3.2f}")
    #esse :>3.2f significa printe 3 casas mais pra direita, com 2 espaços decimais (pros números da tupla)

print("="*50)