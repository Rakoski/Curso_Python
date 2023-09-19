numero = []
while True:
    numero.append(int(input("Digite um número: ")))
    quer_continuar = str(input("Quer continuar? [S/N]: "))
    if "S" in quer_continuar:
        continue
    print(f"O menor número digitado foi {min(numero)}, o maior foi {max(numero)}"
          f" e a sua média é {sum(item for item in numero) / len(numero):.2f}")
