def main():

    frase = str(input("FRASE: "))
    tamanho = len(frase)

    print(tamanho)

    for letra in range(tamanho):
        if frase[tamanho-letra-1:tamanho-letra] != " ":
            print(frase[0:tamanho-letra])


main()