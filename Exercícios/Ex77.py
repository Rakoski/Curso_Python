palavras = ("LINGUAGEM",
            "GARRAFA",
            "FEIRA",
            "LOUÇA",
            "SURPRESA",
            "MARCADOR",
            "CBD")
for p in palavras:#Lembrando que esse \n serve pra quebrar a linha
    print(f'\n palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou': #Se tiver vogal dentro das letras do loop, vulgo as palavras da tupla
            print(letra, end=' ')
