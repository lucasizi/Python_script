def teste():
    salario = int(input("Digite seu salario: "))
    idade = int(input("Digite sua idade: "))
    contri = int(input("Quantos anos de contribuição você possui: "))
    sexo = input("Seu sexo é masculino ou feminino? Digite m ou f (Minusculo!): ")
    apos_m = 65;
    apos_f = 60;
    contri_m = 35;
    contri_f = 30;

    if contri >= idade:
        print(f"Sua contribuição é maior ou igual sua idade, por favor digite informações validas!")
        return;

    if contri >= 35 and sexo == 'm' or contri >= 30 and sexo == 'f':
        print(f"Você possui {contri} de contribuição, isso já te torna apto para ter 100% sua aposentadoria")
        return;

    if contri < 35 and sexo == 'm' and idade >= 65 or contri < 30 and sexo == 'f' and idade >= 62:
        print(
            f"Você possui menos de 35 de contribuição, porém já passa de {idade} anos de idade, isso te torna apto a aposentar com 75% do salario")
        print(f"Com base em seu salario de {salario}, você irá receber em sua aposentadoria {salario * 75 / 100} reais")
        return;

    if sexo == 'm':
        print(
            f"Você possuí {idade} anos de idade, e {contri} de contribuição. Para se aposentar ainda faltam {apos_m - idade} anos pela idade, ou {contri_m - contri} anos pela contribuição")
        return;

    if sexo == 'f':
        print(
            f"Você possuí {idade} anos de idade, e {contri} de contribuição. Para se aposentar ainda faltam {apos_f - idade} anos pela idade, ou {contri_f - contri} anos pela contribuição")
        return;


teste()
