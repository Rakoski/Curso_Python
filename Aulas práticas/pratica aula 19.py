#---------------------------------- BÁSICO DO PRINT() EM UM DICIONÁRIO ----------------------------------------------

#filme = {'titulo': 'Star Wars',
         #'ano': 1977,
          #'diretor': 'George Lucas'
         #}
#print(filme.values())
#print(filme.keys())
#print(filme.items())

#---------------------------------------- COMO DELETAR UM ITEM -----------------------------------------------------
#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#del pessoas["sexo"]
#print(pessoas)

#--------------------------------------- DICIONÁRIOS DENTRO DE LISTAS ----------------------------------------------
brasil = list()
estado = dict()
for contador in range(0, 3):
    estado['uf'] = str(input('Qual seu estado? '))
    estado['sigla'] = str(input('Qual a sigla dele? '))
    brasil.append(estado.copy()) #Lembrar que no dict() não tem [:], por isso precisamos do .copy()
#print(estado1, estado2)
#print(brasil[0], brasil[1])
for estados in brasil:
    for valor in estados.values():
        print(valor, end=' ')
    print()
