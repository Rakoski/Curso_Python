# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações. 1) A quantidade de notas, 2) a maior nota, 3) A menor nota, 4) A média da turma,
# 5) A situação de cada. Adicione também os docstrings da função
def nota(*n, situacao=False):

    """:param n: Not optional. Shows the dictionary of your grades
    :param situacao. Optional. Shows your situation according to the grading system
    for situacao, above 8 is good, between 6 and 8 is reasonable and below 6 is bad.
    Made by Mateus"""

    notas = dict()
    notas['quantidade'] = len(n)
    notas['Maior'] = max(n)
    notas['Menor'] = min(n)
    notas['Média'] = sum(n)/len(n)
    if situacao:
        if notas['Média'] >= 8:
            notas['situacao'] = 'BOA'
        elif notas['Média'] >= 6:
            notas['situacao'] = 'RAZOÁVEL'
        else:
            notas['situacao'] = 'RUIM'
    return notas


# Programa principal
resp = nota(5.4, 6.7, 8.5, 9.2, situacao=True)
print(resp)
help(nota)
