meu_dicionario = {"A":"AMEIXA","B":"BOLA","C":"CACHORRO"}

print(meu_dicionario["C"])

for chave in meu_dicionario:
    print(chave+":"+meu_dicionario[chave])
    print(meu_dicionario[chave])

for i in meu_dicionario.items():
    print(i)