# --------------------------------------------BASICO DO DEF E FUNCOES---------------------------------------------------

# def titulo(msg):
#   print('-' * 30)
#   print(msg)
#   print('-' * 30)


# programa principal
# titulo('    CURSO EM VÍDEO      ')
# titulo('    APRENDA PYTHON      ')
# titulo('    GUSTAVO GUANABARA   ')

# --------------------------------------------------SOMA EM DEF---------------------------------------------------------
# def soma(a, b):  # No caso aqui ele recebe 2 parâmetros "a e b", assim sempre iremos precisar de 2 parâmetros quando
# formos utilizá-lo
#    print(f'A = {a} e B = {b}')
#    s = a + b
#    print(f'A soma de A + B = {s}')
#    print()
# Lembrando que sempre é preciso 2 linhas sem nada após o def até o comando principal


# Programa principal
# soma(a=5, b=4)
# soma(a=7, b=2)

# ----------------------------------------PACKETS, LOOP FOR, DESEMPACOTAMENTO E (*) EM DEF------------------------------
# def contador(*num):
#    tam = len(num)
#    print(f'Recebi os valores {num} e são ao todo {tam} números ')


# contador(8, 0)
# contador(2, 1, 6)
# contador(4, 4, 7, 6, 2)

# -------------------------------------- LISTAS USANDO DEF E COMO DOBRÁ-LAS --------------------------------------------

# def dobra(lst):
#    pos = 0
#    while pos < len(lst):
#        lst[pos] *= 2
#        pos += 1


# valores = [2, 5, 8, 0, 9]
# print(valores)
# dobra(valores)
# print(valores)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = []
for contador in range(0, 5):
    valores.append(int(input('Digite seus valores: ')))
print(valores)
dobra(valores)
print(valores)