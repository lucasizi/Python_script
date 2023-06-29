# faça um programa que receba a idade do usuario e diga se ele é maior ou menor de idade
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor")

# faça um programa que recebas duas notas digitadas pelo usuarios. Se a nota for maior ou igual a seis
# escreva aprovado, senão escreve reprovado

nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))

notas = nota1 + nota2 / 2

if notas < 6:
    print("Reprovado")
else:
    print("Aprovado")
# escreva um programa que resolva uma equacao


# escreva um programa que ordene uma lista numérica com três elementos.
lista = [3, 2, 1]


print(sorted(lista))


# escreva um programa que receba dois numeros e um sinal, e faça a operação matematica de acordo com o sinal

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
operacao = input("Escreva o sinal da operacao: ")

if operacao == "+":
    print(numero1 + numero2)
elif operacao == "-":
    print(numero1 - numero2)
elif operacao == "*":
    print(numero1 * numero2)
elif operacao == "/":
    print(numero1 / numero2)
elif operacao == "**":
    print(numero1 ** numero2)

