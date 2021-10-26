def main():

    salario = float(input("Digite seu salário: "))
    porcentagem = float(input("Digite o quanto você vai economizar por mês: "))
    semestral = float(input("Digite o aumento do salario a partir do 6º mês: "))
    custo_total = float(input("Digite o custo da casa: "))

    vguardado = 0
    contador = 0


    while vguardado < custo_total:
        contador = contador + 1
        if contador % 6 == 0:
            salario = salario + (salario * semestral) / 100
        vguardado = vguardado + (vguardado*(0.04/100))
        vguardado = vguardado + (porcentagem * salario / 100)

    if contador == 1:
        print("Você vai levar", contador, "mes para comprar sua casa")
    if contador > 1 and contador <= 11:
        print("Você vai levar", contador, "meses para comprar sua casa")
    if contador >= 12 and contador < 24:
        print("Você vai levar", contador, "meses para comprar sua casa")
        print("Que é equivalente a", int(contador / 12), "anos e", int((float(contador / 12) - int(contador / 12)) * 12),"Meses")
    if contador >= 24:
        print("Você vai levar", contador, "meses para comprar sua casa")
        print("Que são equivalentes a", int(contador / 12), "anos e", int((float(contador / 12) - int(contador / 12)) * 12),"Meses")


main()