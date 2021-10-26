def main2():
    numero = int(input("insira um numero de 0 a 10: "))

    while numero > 10 or numero < 0:
        numero = int(input("insira um numero valido: "))

    print("Seu numero é", numero)
main2()
