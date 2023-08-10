qtd = int(input("Quantas vezes esse loop deve rodar?: "))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma+num
print(f'A soma é {soma}')




"""
# Exemplo de for 1(iterando em uma string)
for numeros in lista:
    print(numeros, lista)
    

# Exemplo de for 2 (Iterando em uma string)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)


Enumerate:
(0, 'G'), (1, 'E'), (2,'E'), (3,'K')

for indice, letra in enumerate(nome):
    print(nome[indice]) 

"""
