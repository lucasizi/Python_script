def comparar():

    tipo = input("Quer comparar unidades ou gramas? Digite 'u' para unidades ou 'g' para gramas: ")

    if tipo == 'g':
        peso1 = float(input("Peso em gramas produto 1: "))
        valor1 = float(input("valor produto 1: "))

        peso2 = float(input("Peso em gramas produto 2: "))
        valor2 = float(input("valor produto 1: "))

        dif1 = valor1 * 100 / peso1
        dif2 = valor2 * 100 / peso2

        print(f"100 gramas do produto 1 está saindo por R${dif1}")
        print(f"100 gramas do produto 2 está saindo por R${dif2}")

        if dif1 < dif2:
            print(f"O produto 1 compensa mais que o produto 2, pois está R${dif2 - dif1} mais barato")
        else:
            print(f"O produto 2 compensa mais que o produto 1, pois está R${dif1 - dif2} mais barato")

    if tipo == 'u':
        qtd1 = float(input("Unidades produto 1: "))
        valor1 = float(input("Valor produto 1: "))

        qtd2 = float(input("Unidades produto 2: "))
        valor2 = float(input("Valor produto 2: "))

        unidade1 = valor1 / qtd1
        unidade2 = valor2 / qtd2

        print(f"A Unidade do produto 1 sai por  :{unidade1}")
        print(f"A Unidade do produto 2 sai por  :{unidade2}")

        if unidade1 < unidade2:
            print(f"O produto 1 compensa mais que o produto 2, pois a unidade está R${unidade2 - unidade1} mais barata")
        else:
            print(f"O produto 2 compensa mais que o produto 1, pois a unidade está R${unidade1 - unidade2} mais barata")


comparar()
