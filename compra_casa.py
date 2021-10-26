def main ():

    salario = float(input("Digite o seu salario: "))
    casa = float(input("Digite o valor da casa que quer comprar: "))
    economia = float(input("Digite quantos por cento quer economizar por mes: "))
    count = 0;
    banco = 0;

    print("Você consegue economizar um total de ", (economia * salario / 100), "por mês")

    while banco < casa:
          banco = banco + (economia * salario / 100)
          count = count + 1;

    anos = int((count/12))

    if count == 1:
        print("Você levara ", count, "mês para comprar sua casa")

    if count > 1 and count < 12:
        print("Você levara ", count, "meses para comprar sua casa")

    if count == 12:
        print("Você levara ", int((count/12)), "ano para comprar sua casa")

    if count > 12 and count < 24:
        print("Você levara ", int((count/12)), "ano e ", int(((count/12) - (anos)) * 12), "meses para comprar sua casa")

    if count >= 24 and count%12 == 0:
        print("Você levara ", int((count/12)), "anos para comprar sua casa")

    if count >= 24 and count%12 != 0:

        print("Você levara ", int((count/12)), "anos e ", int(((count/12) - (anos)) * 12), "meses para comprar sua casa")

    if banco > casa:
        print("E ainda sobram: ",(banco - casa), "da sua economia na ultima parcela")

main()