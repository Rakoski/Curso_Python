# Faça um programa que tenha uma função chamada escreva(), que receba um texto com qualquer parâmetro e mostre uma men-
# sagem com tamanho adaptável
resposta = 'sim'
def escreva(txt):
    lenght = len(txt)
    print('-' * (lenght + 2))
    print(f' {txt}')
    print('-' * (lenght + 2))


txt = str(input('Digite sua frase: ')).strip()
escreva(txt)