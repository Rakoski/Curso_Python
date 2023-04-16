# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# Retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 16:
        return f'Com {idade} anos, seu voto é NEGADO'
    elif 16 <= idade <= 18:
        return f'Com {idade} anos, seu voto é OPCIONAL'
    else:
        return f'Com {idade} anos, seu voto é OBRIGATÓRIO'


print(voto(2009))

