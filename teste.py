crack = ""
while True:
    user = str(input("Insira seu usuario: "))
    password = str(input("insira sua senha: "))

    if user != password:
        
        for i in range(len(password)):
            crack += "*"

        print("Seu usuario é",user,"e sua senha é",crack)
    
        break

    else:
        print("Usario igual a senha. Insira credenciais validas!.")