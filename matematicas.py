lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = []

def dobro(i):
    if i%2==0:
        return i
lista2 = filter(dobro, lista)
print(lista2)