# Faça um programa chamado ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum não tenha sido informado corretamente
def ficha(nome, numero):
    if nome.isalnum():
        nome = nome
    else:
        nome = '<desconhecido>'
    if numero.isnumeric():
        numero = numero
    else:
        numero = '0'
    print(f'O jogador {nome} marcou {numero} gols no campeonato')


x = str(input('Digite o nome do seu jogador: ')).strip()
y = str(input('Digite quantos gols ele fez: ')).strip()
print(ficha(x, y))
