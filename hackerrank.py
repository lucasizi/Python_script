#operacao bancaria

texto = input("Digite o texto: ")
vogais = "AEIOU"
count = 0

for letra in texto:
    if not letra.upper() in vogais:
        print(letra)

print()

for letra in texto:
    if not letra.upper() in vogais:
        count = count + 1
    
print(count, end="")
print()

for numero in range (0, 11):
    print(numero, end="")
print()
for numero in range (0, 11,2):
    print(numero, end="")
print()
for numero in range (0, 11,6):
    print(numero, end="")
print()


