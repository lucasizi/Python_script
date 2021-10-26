def main():
    user = str(input("Insira seu usuario: "))
    password = str(input("insira sua senha: "))
    tamanho = len(password)

    senha = "*" * tamanho

    while user == password:
        print("Usario igual a senha. Insira credenciais validas!.")
        user = str(input("Insira seu usuario: "))
        password = str(input("insira sua senha: "))

    if user != password:
        print("Seu usuario é",user,"e sua senha é",senha)


main ()